import time
import requests
import json
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def load_urls(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ").strip()

def tokenize(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

def build_index(filepath):
    urls = load_urls(filepath)
    index = {}

    for i, url in enumerate(urls):
        print(f"Indexing ({i+1}/{len(urls)}): {url}")

        try:
            response = requests.get(url, timeout=5)
            html = response.text
        except Exception as e:
            print(f"Failed: {url} — {e}")
            continue

        text = extract_text(html)
        tokens = tokenize(text)

        for token in tokens:
            if token not in index:
                index[token] = []
            if url not in index[token]:
                index[token].append(url)

        time.sleep(0.5)

    return index

# Step 5 - Save index to a file
def save_index(index, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(f"Index saved to {filepath}")

# Run it
index = build_index("urls.txt")
save_index(index, "index.json")