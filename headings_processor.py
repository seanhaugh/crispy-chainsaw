# headings_processor.py

import requests
from bs4 import BeautifulSoup

def extract_headings(url):
    """
    Extract headings from a given URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headings = []
    for level in range(1, 7):
        for heading in soup.find_all(f'h{level}'):
            text = heading.get_text().strip()
            if text:
                headings.append(text)
    return headings

def consolidate_headings(competitors):
    """
    Extract and consolidate headings from all competitor URLs.
    """
    all_headings = []
    for competitor in competitors:
        headings = extract_headings(competitor)
        all_headings.extend(headings)
    # Remove duplicates while preserving order
    seen = set()
    consolidated_headings = []
    for heading in all_headings:
        if heading not in seen:
            seen.add(heading)
            consolidated_headings.append(heading)
    return consolidated_headings
