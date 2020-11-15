from urllib.parse import urlparse
import re
from lxml import html
import requests
from bs4 import BeautifulSoup


emails  = []

page = requests.get('https://www.dentalplanet.com')
source = page.text
soup = BeautifulSoup(source, "html.parser")

for a in soup.find_all('a', href=True):
    print (a['href'])



