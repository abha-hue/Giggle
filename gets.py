import time
import requests
from collections import deque
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links(url):
    response = requests.get(url, timeout=5)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    links = set()
    for tag in soup.find_all("a", href=True):
        raw_link = tag["href"]
        absolute_link = urljoin(url, raw_link)
        clean_link = absolute_link.split("#")[0]
        if urlparse(clean_link).scheme in ("http", "https"):
            links.add(clean_link)

    return html, links

def same_domain(url, start_url):
    return urlparse(url).netloc == urlparse(start_url).netloc

def crawl(start_url, max_pages=50):
    visited = set()
    queue = deque([start_url])
    pages = {}

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        try:
            html, links = get_links(url)
        except Exception as e:
            print(f"Failed: {url} — {e}")
            continue

        visited.add(url)
        pages[url] = html
        print(f"Crawling ({len(visited)}/{max_pages}): {url}")

        for link in links:
            if link not in visited and same_domain(link, start_url):
                queue.append(link)

        time.sleep(0.5)

    return pages

crawled_pages = crawl("http://books.toscrape.com/")