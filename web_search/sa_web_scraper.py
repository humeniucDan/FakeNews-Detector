import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

def search_web(query: str, first_results: int = 2) -> list:
    params = {
        "engine": "google",
        "q": query,
        "num": first_results,
        "api_key": os.getenv('SERPAPI_KEY')  # Replace with your actual API key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    links = []
    for result in results.get("organic_results", [])[:first_results]:
        link = result.get("link")
        if link:
            links.append(link)

    return links

results = search_web('nicusor dan are media generala bac 7.4')
for result in results:
    print(result)