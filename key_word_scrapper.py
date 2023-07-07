import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def web_scraper(base_url, keywords):
    visited_links = set()
    links_to_visit = [base_url]
    matched_links = []

    while links_to_visit:
        url = links_to_visit.pop(0)
        if url not in visited_links:
            try:
                response = requests.get(url)
                visited_links.add(url)
            except requests.exceptions.RequestException as e:
                print(f"RequestException on site {url}")
                continue
            soup = BeautifulSoup(response.text, 'lxml')
            for link in soup.find_all('a', href=True):
                possible_link = link['href']
                if is_valid(possible_link):
                    absolute_link = urljoin(url, possible_link)
                    if absolute_link not in visited_links:
                        links_to_visit.append(absolute_link)
            
            page_text = soup.get_text().lower()
            for keyword in keywords:
                if keyword.lower() in page_text:
                    print(f"Found keyword {keyword} on page {url}")
                    matched_links.append(url)

    return matched_links

# Usage:
base_url = "https://www.wpri.com"
keywords = ["security", "breach" "hacked"]
print(web_scraper(base_url, keywords))
