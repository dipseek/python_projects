import cv2
import dlib
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Load face detector and predictor
predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

def extract_index_nparray(nparray):
    return nparray[0][0]

def get_landmarks(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) == 0:
        return None
    landmarks = predictor(gray, faces[0])
    return np.array([(p.x, p.y) for p in landmarks.parts()], dtype=np.int32)

def triangulate(points, hull):
    rect = cv2.boundingRect(hull)
    subdiv = cv2.Subdiv2D(rect)
    for p in hull:
        subdiv.insert((float(p[0]), float(p[1])))
    triangles = subdiv.getTriangleList()
    triangles = np.array(triangles, dtype=np.int32)

    indexes = []
    for t in triangles:
        pt1, pt2, pt3 = (t[0], t[1]), (t[2], t[3]), (t[4], t[5])
        index1 = np.where((points == pt1).all(axis=1))
        index2 = np.where((points == pt2).all(axis=1))
        index3 = np.where((points == pt3).all(axis=1))
        if index1[0].size and index2[0].size and index3[0].size:
            indexes.append([
                extract_index_nparray(index1),
                extract_index_nparray(index2),
                extract_index_nparray(index3)
            ])
    return indexes

def warp_triangle(img1, img2, t1, t2):
    rect1 = cv2.boundingRect(np.float32([t1]))
    rect2 = cv2.boundingRect(np.float32([t2]))

    t1_rect = [((t1[i][0] - rect1[0]), (t1[i][1] - rect1[1])) for i in range(3)]
    t2_rect = [((t2[i][0] - rect2[0]), (t2[i][1] - rect2[1])) for i in range(3)]

    mask = np.zeros((rect2[3], rect2[2], 3), dtype=np.float32)
    cv2.fillConvexPoly(mask, np.int32(t2_rect), (1.0, 1.0, 1.0), 16, 0)

    img1_rect = img1[rect1[1]:rect1[1]+rect1[3], rect1[0]:rect1[0]+rect1[2]].astype(np.float32)
    size = (rect2[2], rect2[3])
    warp_mat = cv2.getAffineTransform(np.float32(t1_rect), np.float32(t2_rect))
    img2_rect = cv2.warpAffine(img1_rect, warp_mat, size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)

    img2_rect = img2_rect * mask

    # Get region of img2 and cast it to float32 for safe math
    img2_part = img2[rect2[1]:rect2[1]+rect2[3], rect2[0]:rect2[0]+rect2[2]].astype(np.float32)
    img2_part = img2_part * (1.0 - mask)
    result = img2_part + img2_rect

    # Convert back to uint8
    img2[rect2[1]:rect2[1]+rect2[3], rect2[0]:rect2[0]+rect2[2]] = np.clip(result, 0, 255).astype(np.uint8)

def swap_faces(img1_path, img2_path, output_path="face_swapped.jpg"):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    points1 = get_landmarks(img1)
    points2 = get_landmarks(img2)
    if points1 is None or points2 is None:
        messagebox.showerror("Error", "No face detected in one of the images.")
        return

    hull1 = cv2.convexHull(points1, returnPoints=True).reshape(-1, 2)
    hull2 = cv2.convexHull(points2, returnPoints=True).reshape(-1, 2)
    indexes = triangulate(points2, hull2)

    img2_new_face = np.zeros_like(img2)
    for triangle_index in indexes:
        t1 = [points1[i] for i in triangle_index]
        t2 = [points2[i] for i in triangle_index]
        warp_triangle(img1, img2_new_face, t1, t2)

    mask = np.zeros_like(img2[:, :, 0])
    cv2.fillConvexPoly(mask, hull2, 255)
    center = (int(np.mean(hull2[:, 0])), int(np.mean(hull2[:, 1])))

    output = cv2.seamlessClone(np.uint8(img2_new_face), img2, mask, center, cv2.NORMAL_CLONE)
    cv2.imwrite(output_path, output)
    show_result(output_path)

def show_result(image_path):
    result_window = tk.Toplevel()
    result_window.title("Face Swapped Result")

    img = Image.open(image_path)
    img = img.resize((400, 400))
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(result_window, image=img_tk)
    label.image = img_tk
    label.pack()

def select_image1():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if path:
        entry1.delete(0, tk.END)
        entry1.insert(0, path)

def select_image2():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if path:
        entry2.delete(0, tk.END)
        entry2.insert(0, path)

def run_swap():
    path1 = entry1.get()
    path2 = entry2.get()
    if not path1 or not path2:
        messagebox.showwarning("Warning", "Please select both images.")
        return
    swap_faces(path1, path2)

# --- GUI Setup ---
root = tk.Tk()
root.title("Face Swapper")
root.geometry("500x250")

tk.Label(root, text="Image 1 Path:").pack()
entry1 = tk.Entry(root, width=50)
entry1.pack()
tk.Button(root, text="Browse Image 1", command=select_image1).pack(pady=5)

tk.Label(root, text="Image 2 Path:").pack()
entry2 = tk.Entry(root, width=50)
entry2.pack()
tk.Button(root, text="Browse Image 2", command=select_image2).pack(pady=5)

tk.Button(root, text="Swap Faces", command=run_swap, bg="green", fg="white").pack(pady=20)

root.mainloop()
