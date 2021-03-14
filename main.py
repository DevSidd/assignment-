import requests
from bs4 import BeautifulSoup

URL = 'https://store.hp.com/us/en/pdp/hp-laptop-15t-dy200-2j130av-1'

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

URL = "https://store.hp.com/us/en/pdp/hp-laptop-15t-dy200-2j130av-1"
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")

print(soup.prettify())

title = soup.find_all('h3',class_='bv-content-title')

title

review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title

review_title[0:1] = [title.lstrip('\n') for title in review_title]
review_title

review_title[0:1] = [title.rstrip('\n') for title in review_title]
review_title