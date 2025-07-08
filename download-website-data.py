import requests
from bs4 import BeautifulSoup

def download_and_prettify_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        
        pretty_html = soup.prettify()
        with open('page.html', 'w', encoding='utf-8') as html_file:
            html_file.write(pretty_html)

        
        text_data = soup.get_text(separator='\n')
        cleaned_text = '\n'.join(line.strip() for line in text_data.splitlines() if line.strip())

        with open('page_text.txt', 'w', encoding='utf-8') as text_file:
            text_file.write(cleaned_text)

        print("✅ Prettified HTML and cleaned text saved successfully.")

    except requests.RequestException as e:
        print(f"❌ Error fetching the page: {e}")

download_and_prettify_page('https://netflix.com')
