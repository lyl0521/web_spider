import re
from lxml import etree
import requests
import MySQLdb


db_conn = None
db_cursor = None

def initMySQL():
    global db_cursor
    global db_conn

    host = 'localhost'
    user = 'root'
    password = 'mysql'
    db = 'db_douban'
    db_conn = MySQLdb.connect(host = host , user = user ,password = password , db = db ,charset = 'utf8')

    db_cursor = db_conn.cursor()

def parse(url):
    global db_cursor

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


        sql = "insert into db_douban.movie(name,star,comment,url,director,actor) values ('%s','%s','%s','%s','%s','%s')"%(name,star,comment,url,director,actor[0])
        # value = (name,star)
        db_cursor.execute(sql)






    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url :
        next_url = 'https://movie.douban.com/top250'+next_url[0]
        parse(next_url)

if __name__ == '__main__':
    initMySQL()
    parse('https://movie.douban.com/top250')
    db_conn.commit()

    db_cursor.close()
    db_conn.close()