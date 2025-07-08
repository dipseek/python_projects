import os

while True:
    print("""
    -------- Menu --------
    1. Open Chrome
    2. Open Notepad
    3. Open Google.com
    4. Open YouTube.com
    5. Exit
    """)

    choice = input("Enter your choice (1–5): ")

    if choice == "1":
        os.system("start chrome")  # 'start' ensures it works on Windows
    elif choice == "2":
        os.system("notepad")
    elif choice == "3":
        os.system("start chrome www.google.com")
    elif choice == "4":
        os.system("start chrome www.youtube.com")
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
