import requests
from bs4 import BeautifulSoup

def search_web(query: str, first_results: int = 1):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # DuckDuckGo search URL (HTML version)
    url = 'https://html.duckduckgo.com/html/'
    params = {
        'q': query
    }

    response = requests.post(url, data=params, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for link in soup.find_all('a', {'class': 'result__a'}, limit=first_results):
        href = link.get('href')
        if href:
            results.append(href)

    return results

if __name__ == "__main__":
    results = search_web('nicusor dan are media generala bac 7.4')
    for result in results:
        print(result)