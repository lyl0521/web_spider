from lxml import etree
import requests
import re

html = requests.get('https://movie.douban.com/top250?start=0&filter=')
selector = etree.HTML(html.text)

movie_list = selector.xpath("//ol[@class='grid_view']/li")
all_movie = []

for movie in movie_list:
    name = movie.xpath(".//div[@class='hd']/a/span[1]/text()")[0]  # 电影名称
    info = movie.xpath(".//div[@class='bd']/p[1]/text()")[0].strip('\n').strip(' ')  # 电影信息
    star = movie.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]  # 电影评分
    comment = movie.xpath(".//div[@class='star']/span[4]/text()")[0]  # 电影评论人数
    url = movie.xpath(".//div[@class='hd']/a/@href")[0]
    comment = comment.strip('人评价')
    director = re.findall("导演: (.*?) ", info)[0]
    actor = re.findall("主演: (.*?) ", info)
    if not actor:
        act = "未知"
    print(type(actor))
    movie_info = [str(name), str(star), str(director), str(actor), str(comment), str(url)]
    all_movie.append(movie_info)

print(all_movie)
