# serp.py

import requests
from bs4 import BeautifulSoup

def get_competitors(keyword, num_competitors=5):
    """
    Scrape the SERP to get top competitors for the given keyword.
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    query = keyword.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    competitors = []
    for g in soup.find_all('div', class_='yuRUbf')[:num_competitors]:
        link = g.find('a')['href']
        competitors.append(link)
    
    return competitors
