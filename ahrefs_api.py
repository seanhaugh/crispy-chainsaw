import requests

def get_target_keywords(competitors):
    """
    Use the Ahrefs API to get top keywords for the given competitors.
    """
    # Replace with your Ahrefs API token
    API_TOKEN = 'YOUR_AHREFS_API_TOKEN'
    target_keywords = set()
    
    for competitor in competitors:
        endpoint = f"https://apiv2.ahrefs.com?token={API_TOKEN}&from=domain_organic_keywords&target={competitor}&limit=10&mode=domain"
        response = requests.get(endpoint)
        data = response.json()
        for keyword_info in data.get('keywords', []):
            target_keywords.add(keyword_info['keyword'])
    
    return list(target_keywords)
