# https://stackoverflow.com/questions/4462061/beautiful-soup-to-parse-url-to-get-another-urls-data


import requests
from bs4 import BeautifulSoup

result = requests.get('http://minneapolis.eventful.com/events/categories/music') # ?page_number=2
c = result.content
soup = BeautifulSoup(c, "html.parser")

# soup.prettify()

# print(soup)

for anchor in soup.findAll('a', href=True):
    print(anchor['href'])
