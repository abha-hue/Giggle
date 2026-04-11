import requests
from bs4 import BeautifulSoup
import queue
URL = "https://www.geeksforgeeks.org/"
resp = requests.get(URL)
soup = BeautifulSoup(resp.content, 'html.parser')
ls = soup.find_all('a')

for i in ls:
    queue.put(i.get('href'))
    print(i.get('href'))
