import requests
from bs4 import BeautifulSoup
inp = "https://en.wikipedia.org/wiki/Google"
page = requests.get(inp).text
soup = BeautifulSoup(page,"html.parser")


urls =["https://en.wikipedia.org/wiki/Google"]
text="input"
list = ['h1', 'h2', 'h3', 'p', 'a', 'ul', 'span', 'input']

with open(str(text) +'.txt','w',encoding='utf-8') as outfile:
    for url in urls:
        website = requests.get(url)
        soup = BeautifulSoup(website.content, "lxml")
        tags = soup.find_all(list)
        text = ["".join(s.findAll(text=True)) for s in tags]
        text_len = len(text)
        for item in text:
            print(item, file=outfile)