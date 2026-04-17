from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["sprinting", "sprinter", "sprinter's", "sprinted", "runs", "running", "runner", "runner's"]
sentence = "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"

newsentnce = word_tokenize(sentence)
print(type(newsentnce))

for w in words:
    print(f"{w} -> {ps.stem(w)}")

