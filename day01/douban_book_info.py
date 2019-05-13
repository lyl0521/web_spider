import re
import requests
from lxml import etree

def parse(url):

    html = requests.get(url)
    selector = etree.HTML('html.text')
    book_list = selector.xpath("//div[@class='indent']/table/tbody/tr[@class='item']/td[2]")

    all_book = []

    for book in book_list:

        name = selector.xpath(".//div[@class='p12']/a/text()")[0]
        print(type(name))
        # book_info = [name]
        # all_book.append(name)




if __name__ == '__main__':
    parse('https://book.douban.com/top250')