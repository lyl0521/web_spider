from bs4 import BeautifulSoup
from lxml import etree
import re
import requests

html = requests.get('https://movie.douban.com/top250')
html = html.text

soup = BeautifulSoup(html,'lxml')
#
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
code = soup.find_all(attrs={'class':'grid_view'})


