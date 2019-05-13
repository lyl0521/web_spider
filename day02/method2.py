import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
cookie = 'bid=G5fxsPUKEUg; ll="118174"; _vwo_uuid_v2=D02835AC411C4FABD3F4F6DEB6FF9D390|bd98031750acd1a8e175844b4ccd8442; __yadk_uid=KMqhE3yVCjEtxiFMwxlw4oakWe59jnCV; gr_user_id=38b08483-e3f5-49d6-b8cc-dee6b9669f9c; viewed="1770782_1007622"; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1557711036%2C%22https%3A%2F%2Faccounts.douban.com%2Faccounts%2Fpassport%2Fregister%22%5D; _pk_ses.100001.8cb4=*; __gads=ID=8efa50b0ce9d479c:T=1557711033:S=ALNI_MZGX437ATPzwcjJmpa0-xauMo8VaQ; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19640; douban-fav-remind=1; trc_cookie_storage=taboola%2520global%253Auser-id%3Df4994f42-755d-4961-9322-d9eef0733155-tuct3c91f52; __utma=30149280.1927037011.1555593668.1557710188.1557711187.12; __utmz=30149280.1557711187.12.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=30149280; dbcl2="196408600:sDeSfpKEMnk"; ck=inyI; _pk_id.100001.8cb4=62eb5581ebe10270.1556586326.4.1557715647.1557574424.; __utmt=1; __utmb=30149280.41.10.1557711187'


cookie_list = cookie.split(';')

cookie_dict = {}

for cookie in cookie_list:
    key = cookie.split("=")[0].replace(' ','')
    value = cookie.split('=')[1]
    cookie_dict[key] = value

html = requests.get('https://www.douban.com/people/196408600/notes',headers=headers,cookies=cookie_dict)
print(html.text)


"""
从文件中获取cookies:


with open('cookies.txt','r',encoding='utf-8') as f:
    cookies_str = f.readline()

cookie_list = cookies_str.split(';')
cookie_dict = {}

for cookie in cookie_list:
    key = cookie.split('=')[0].replace(' ','')
    value = cookie.split('=')[1]
    cookie_dict[key] = value

html = requests.get('https://www.douban.com/people/196408600/notes',headers = headers,cookies=cookie_dict)
# print(html.text)
print(html.text)

"""