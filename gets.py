import time
from collections import deque
from urllib.parse import urlparse

def same_domain(url, start_url):
    return urlparse(url).netloc == urlparse(start_url).netloc

def crawl(start_url, max_pages=50):
    visited = set()
    queue = deque([start_url])
    pages = {}                        # stores url → html

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