import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser

def scrape_duckduckgo(query):
    url = "https://html.duckduckgo.com/html/"
    data = {"q": query}
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.post(url, data=data, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return [("❌ Error fetching results.", str(e))]

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for result in soup.find_all('a', class_='result__a', limit=10):
        title = result.get_text()
        link = result['href']
        results.append((title, link))

    return results if results else [("⚠️ No results found.", "")]

def search():
    query = entry.get().strip()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return

    results_box.delete('1.0', tk.END)
    results = scrape_duckduckgo(query)

    with open("results.txt", "w", encoding="utf-8") as f:
        for i, (title, link) in enumerate(results, 1):
            result_text = f"{i}. {title}\n   {link}\n\n"
            results_box.insert(tk.END, result_text)
            f.write(result_text)

    if len(results) == 1 and results[0][1].startswith("http") is False:
        messagebox.showerror("Search Failed", results[0][0])
    else:
        messagebox.showinfo("Success", "Results saved to results.txt")

def copy_selected():
    try:
        root.clipboard_clear()
        selected_text = results_box.get(tk.SEL_FIRST, tk.SEL_LAST)
        root.clipboard_append(selected_text)
        messagebox.showinfo("Copied", "Selected text copied to clipboard.")
    except tk.TclError:
        messagebox.showwarning("No selection", "Please select some text to copy.")

root = tk.Tk()
root.title("DuckDuckGo Search Tool")
root.geometry("650x550")

tk.Label(root, text="🔎 Enter search query:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Search", font=("Arial", 12), command=search).pack(pady=10)

results_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=20, font=("Arial", 10))
results_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Button(root, text="Copy Selected", font=("Arial", 10), command=copy_selected).pack(pady=5)

root.mainloop()
