import re
from lxml import etree
import requests

def parse(url):

    html = requests.get(url)

    selector = etree.HTML(html.text)

    all_movie = []

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
        movie_info = [name, star, director, actor[0], comment, url]
        all_movie.append(movie_info)

    print(all_movie)

    for movie in all_movie:
        info = movie[0]+','+movie[1]+','+movie[2]+','+movie[3]+','+movie[4]+','+movie[5]+'\n'
        with open('movie.txt','a',encoding='utf-8') as f:
            f.write(info)

    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url :
        next_url = 'https://movie.douban.com/top250'+next_url[0]
        parse(next_url)

if __name__ == '__main__':
    parse('https://movie.douban.com/top250')