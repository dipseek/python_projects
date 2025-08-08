try:
    import requests
    from bs4 import BeautifulSoup
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Note: requests/beautifulsoup4 modules not available. Installing with: pip install requests beautifulsoup4")

def scrape_duckduckgo(query):
    """Search DuckDuckGo and return results"""
    if not REQUESTS_AVAILABLE:
        return [("Demo result 1", "https://example.com/1"), 
                ("Demo result 2", "https://example.com/2"),
                ("Demo result 3", "https://example.com/3")]
    
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

def search_demo():
    """Demonstrate web search functionality"""
    
    print("=" * 50)
    print("WEB SEARCH DEMONSTRATION")
    print("=" * 50)
    
    # Demo search query
    query = "Python programming"
    print(f"Search Query: {query}")
    
    if not REQUESTS_AVAILABLE:
        print("\nNote: Using demo results (requests/beautifulsoup4 not available)")
        print("Install with: pip install requests beautifulsoup4")
    
    print("\nSearching DuckDuckGo...")
    results = scrape_duckduckgo(query)
    
    if results and not results[0][1].startswith("❌") and not results[0][1].startswith("⚠️"):
        print(f"\nSUCCESS: Found {len(results)} results:")
        print("-" * 50)
        
        for i, (title, link) in enumerate(results, 1):
            print(f"{i}. {title}")
            print(f"   URL: {link}")
            print()
        
        # Save results to file
        with open("search_results.txt", "w", encoding="utf-8") as f:
            f.write(f"Search Query: {query}\n")
            f.write("=" * 50 + "\n\n")
            for i, (title, link) in enumerate(results, 1):
                f.write(f"{i}. {title}\n")
                f.write(f"   URL: {link}\n\n")
        
        print("Results saved to 'search_results.txt'")
        print("\nSUCCESS: Web search completed successfully!")
        
    else:
        print("FAILED: Search failed or no results found")
        if results:
            print(f"Error: {results[0][0]}")
    
    print("=" * 50)

if __name__ == "__main__":
    search_demo()
