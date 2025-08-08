import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import random
import io


def generate_random_image(width, height):
    array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img = Image.fromarray(array)
    return img


def update_image():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        status_label.config(text="Enter valid integers for width and height.")
        return

    img = generate_random_image(width, height)
    img.thumbnail((400, 400))  
    img_tk = ImageTk.PhotoImage(img)

    image_label.img = img_tk
    image_label.config(image=img_tk)
    status_label.config(text="Random image generated.")


def save_image():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        img = generate_random_image(width, height)
        filename = f"random_image3.png"
        img.save(filename)
        status_label.config(text=f"Saved as {filename}")
    except Exception as e:
        status_label.config(text=f"Error saving image: {e}")


root = tk.Tk()
root.title("Random Image Generator")
root.geometry("500x600")

tk.Label(root, text="Width:").pack()
width_entry = tk.Entry(root)
width_entry.insert(0, "256")
width_entry.pack()

tk.Label(root, text="Height:").pack()
height_entry = tk.Entry(root)
height_entry.insert(0, "256")
height_entry.pack()

ttk.Button(root, text="Generate Image", command=update_image).pack(pady=10)
ttk.Button(root, text="Save Image", command=save_image).pack(pady=5)

image_label = tk.Label(root)
image_label.pack(pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
