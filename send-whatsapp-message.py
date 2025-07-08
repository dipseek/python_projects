import pywhatkit as kit
import tkinter as tk
from tkinter import messagebox
import re
import threading
from datetime import datetime, timedelta

def send_whatsapp_message():
    phone_number = phone_entry.get().strip()
    message = message_entry.get("1.0", tk.END).strip()
    time_input = time_entry.get().strip()

    if not phone_number or not message or not time_input:
        messagebox.showerror("Error", "Please enter phone number, message, and time.")
        return

    phone_pattern = re.compile(r"^\+\d{1,3}\d{6,14}$")
    if not phone_pattern.match(phone_number):
        messagebox.showerror("Error", "Invalid phone number format. Use +[country code][6-14 digits].")
        return

    time_pattern = re.compile(r"^(2[0-3]|[01]?[0-9]):([0-5][0-9])$")
    if not time_pattern.match(time_input):
        messagebox.showerror("Error", "Invalid time format. Use HH:MM (e.g., 09:51).")
        return

    try:
        hour, minute = map(int, time_input.split(":"))
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            messagebox.showerror("Error", "Hour must be 0-23 and minute must be 0-59.")
            return

        now = datetime.now()
        scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        is_next_day = False
        if scheduled_time <= now:
            scheduled_time = scheduled_time + timedelta(days=1)
            is_next_day = True

        if (scheduled_time - now).total_seconds() < 25:
            messagebox.showerror("Error", "Scheduled time is too close. Please choose a time at least 25 seconds in the future.")
            return

        status_text = f"Message will be sent at {hour:02d}:{minute:02d}"
        if is_next_day:
            status_text += " tomorrow"
        status_label.config(text=status_text, fg="blue")
        status_label.pack(pady=5)
        root.update()

        schedule_message = f"Message scheduled for {hour:02d}:{minute:02d}"
        if is_next_day:
            schedule_message += " (tomorrow)"
        messagebox.showinfo("Success", schedule_message)

        def send_message():
            try:
                kit.sendwhatmsg(phone_number, message, hour, minute)
                root.after(0, lambda: status_label.config(text="Message sent!", fg="green"))
                root.after(0, lambda: messagebox.showinfo("Confirmation", f"Message has been successfully sent to {phone_number} at {hour:02d}:{minute:02d}!"))
            except kit.exceptions.CountryCodeException:
                root.after(0, lambda: status_label.config(text="Error: Invalid phone number", fg="red"))
                root.after(0, lambda: messagebox.showerror("Error", "Invalid phone number format. Use +[country code][number]."))
            except Exception as e:
                root.after(0, lambda: status_label.config(text="Error occurred", fg="red"))
                root.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {e}"))

        threading.Thread(target=send_message, daemon=True).start()

    except ValueError:
        status_label.config(text="Error: Invalid time format", fg="red")
        messagebox.showerror("Error", "Invalid time format. Use HH:MM.")

root = tk.Tk()
root.title("WhatsApp Message Scheduler")
root.geometry("400x350")
root.resizable(False, False)  

phone_label = tk.Label(root, text="Phone Number (+[country code][number]):")
phone_label.pack(pady=10)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()
phone_entry.focus()  

time_label = tk.Label(root, text="Time (HH:MM, 24-hour format):")
time_label.pack(pady=10)
time_entry = tk.Entry(root, width=30)
time_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack(pady=10)
message_entry = tk.Text(root, height=5, width=30)
message_entry.pack()

status_label = tk.Label(root, text="")
status_label.pack_forget()  


send_button = tk.Button(root, text="Schedule Message", command=send_whatsapp_message)
send_button.pack(pady=20)

root.mainloop()