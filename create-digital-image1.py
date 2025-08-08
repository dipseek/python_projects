from PIL import Image, ImageDraw
import random

def create_digital_image(width, height, output_file):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    for _ in range(100):
        x0 = random.randint(0, width)
        y0 = random.randint(0, height)
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line((x0, y0, x1, y1), fill=color, width=2)
    image.save(output_file)
    print(f"Image saved as {output_file}")

if __name__ == "__main__":
    create_digital_image(800, 600, "random_image1.png")