import re

import requests
from bs4 import BeautifulSoup

def extract_text(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove script and style elements
    for script_or_style in soup(['script', 'style', 'noscript']):
        script_or_style.extract()

    text = soup.get_text(separator=' ', strip=True)
    clean_text = re.sub(r'\s+', ' ', text).strip()

    return clean_text

print(
    extract_text(
        'https://www.newstatesman.com/culture/music/2017/05/goodbye-greatest-billionaire-lesbian-couple-never-existed'
    )
)