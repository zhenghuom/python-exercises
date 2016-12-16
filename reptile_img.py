#endcoding:UTF-8
'''
爬取图片
'''

import re
from urllib import request
from bs4 import BeautifulSoup
import os

new_urls = set()
old_urls = set()

#参数 url, 储存位置
def savePageInfo( url, path):

    response = request.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html,'html.parser')

    #新的url
    Nav_cont = soup.select('div .ShowNav > a')
    for nav in Nav_cont:
        new_url = nav['href']
        set_new_url(new_url)

    #图片url
    srcs = soup.find_all('img',src = re.compile(r'.+?\.jpg$'))

    if not os.path.isdir(path):
        os.makedirs(path)

    count = 1
    for src in srcs:
        print(src['src'])
        #保存图片
        # response1 = request.urlopen(src['src'])
        # img_cont = response1.read()
        # img_path = path + '/' + str(count) + '.jpg'
        #
        # with open(img_path, 'wb') as file:
        #     file.write(img_cont)
        #
        # count = count + 1
        # file.close()
    print('*******************************************')
#获取新的url
def get_new_url():
    url = new_urls.pop()
    old_urls.add(url)
    return url

#添加图片
def set_new_url(url):
    if len(url) > 0 and url not in new_urls and url not in old_urls:
        new_urls.add(url)

# 要爬的网址
url = 'http://www.umei.cc'
path = "/home/zhm/www/python/hello/learn/img"
new_urls.add(url)

while len(new_urls):
    new_url = get_new_url()
    savePageInfo(new_url, path)


print('ok')

