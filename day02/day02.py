import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}

data = {
    'ck':'',
    'name':'18649181766',
    'password':'19960521lyl',
    'remember':'true',
    'ticket':''
}

url = 'https://accounts.douban.com/j/mobile/login/basic'

session = requests.Session()
result = session.post(url,data=data,headers=header)

html = session.get('https://www.douban.com/people/196408600/notes',headers = header)

print(html.text)
print(result.text)

