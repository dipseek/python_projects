import tkinter as tk
import psutil

def update_ram_info():
    ram = psutil.virtual_memory()

    total = f"{ram.total / (1024 ** 3):.2f} GB"
    available = f"{ram.available / (1024 ** 3):.2f} GB"
    used = f"{ram.used / (1024 ** 3):.2f} GB"
    percent = f"{ram.percent}%"

    total_label.config(text=f"Total RAM: {total}")
    available_label.config(text=f"Available RAM: {available}")
    used_label.config(text=f"Used RAM: {used}")
    percent_label.config(text=f"RAM Usage Percentage: {percent}")

    root.after(1000, update_ram_info)

root = tk.Tk()
root.title("RAM Usage Monitor")
root.geometry("300x180")
root.resizable(False, False)

title_label = tk.Label(root, text="System RAM Usage", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

total_label = tk.Label(root, text="", font=("Helvetica", 12))
total_label.pack()

available_label = tk.Label(root, text="", font=("Helvetica", 12))
available_label.pack()

used_label = tk.Label(root, text="", font=("Helvetica", 12))
used_label.pack()

percent_label = tk.Label(root, text="", font=("Helvetica", 12))
percent_label.pack()

update_ram_info()

root.mainloop()
