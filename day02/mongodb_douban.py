import re
from lxml import etree
import requests
import pymongo


db_client = None
db_corsur = None

def initMongoDB():
    global db_client
    global db_collection

    db_client = pymongo.MongoClient()

    db = db_client['db_douban']
    db_collection = db['movie']




def parse(url):
    global db_cursor

    html = requests.get(url)

    selector = etree.HTML(html.text)


    movie_list = selector.xpath("//ol[@class='grid_view']/li")

    for movie_selector in movie_list:

        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]  # 电影名称
        info = movie_selector.xpath(".//div[@class='bd']/p[1]/text()")[0].strip('\n').strip(' ')  # 电影信息
        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]  # 电影评分
        comment = movie_selector.xpath(".//div[@class='star']/span[4]/text()")[0]  # 电影评论人数
        url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0]
        comment = comment.strip('人评价')
        director = re.findall("导演: (.*?) ", info)[0]
        actor = re.findall("主演: (.*?) ", info)
        if not actor:
            actor = ["未知"]

        movie={
            'name':name,
            'star':star,
            'comment':comment,
            'url':url,
            'director':director,
            'actor':actor
        }

        db_collection.insert_one(movie)





    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url :
        next_url = 'https://movie.douban.com/top250'+next_url[0]
        parse(next_url)

if __name__ == '__main__':
    initMongoDB()
    parse('https://movie.douban.com/top250')

    db_client.close()