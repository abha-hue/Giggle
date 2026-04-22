import json
from indexer import tokenize  # reuse the same tokenize function

# Step 1 - Load index
def load_index(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        index = json.load(f)
    return index

# Step 2 - Search
def search(query, index):
    
    # Clean the query same way as indexing
    tokens = tokenize(query)

    if not tokens:
        return []

    # Step 3 - Look up each word and count matches per URL
    url_score = {}  # { url: number of query words it matched }

    for token in tokens:
        if token in index:
            for url in index[token]:
                if url not in url_score:
                    url_score[url] = 0
                url_score[url] += 1  # increment match count

    # Step 4 - Sort by score (highest first)
    ranked = sorted(url_score.items(), key=lambda x: x[1], reverse=True)

    return ranked