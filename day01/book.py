import re
import requests
from lxml import etree


headers={'User_Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}


def parse(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)

    book_list = selector.xpath("//tr[@class='item']")
    #
    all_book = []
#
    for book in book_list:
    # name = selector.xpath("//div[@class='indent']/table/tr[@class='item']/td[2]/div[@class='p12']/a/text()")[0].strip('\n').strip(' ')

        name = book.xpath(".//td/div/a/@title")[0]
        info = book.xpath(".//td/p[1]/text()")[0]     #为什么+[0] 重复输出
        url = book.xpath(".//td/div/a/@href")[0]
        star = book.xpath(".//td/div/span[2]/text()")[0]
        comment = book.xpath(".//td/div/span[3]/text()")[0].strip('(').strip('\n').strip(' ').strip(')').strip(' ').strip('\n')
        author = re.findall("(.*?) /",info)[0]
        # translater = re.findall("/ (.*?) / (.*?) / (.*?) /",info)[0]
        translater = re.findall("/ (.*?) /",info)[0]
        # publisher = re.findall("/ .*? / (.*?) /",info)[0]
        book_info = [name,author,translater,star,comment,url]
        print(book_info)
        all_book.append(book_info)
    #

    #
    for book in all_book:
        info = book[0]+','+book[1]+','+book[2]+','+book[3]+','+book[4]+','+book[5]+'\n'
        with open('book.txt', 'a', encoding='utf-8') as f:
            f.write(info)

    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url:
        next_url = next_url[0]
        parse(next_url)


if __name__ == '__main__':
    parse('https://book.douban.com/top250?start=0')