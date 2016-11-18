# -*- coding:utf-8 -*-
"""
@version: ??
@author: jackieyan
@license: Apache Licence 
@contact: yanjiankai4618@gmail.com
@site: 
@software: IntelliJ IDEA
@file: Demo3.py
@time: 2016/11/15 10:05
"""
import re


from pip._vendor import requests

# r = re.compile(r'<script src="(js\/.+?\.js)"><\/script>'
html = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%BB%C6%BD%F0%CA%A5%D2%C2&fr=ala&ori_query=%E9%BB%84%E9%87%91%E5%9C%A3%E8%A1%A3&ala=0&alatpl=sp&pos=0')
r = re.compile(r'http:\/\/.+?\.jpg')
te = 'data-imgurl="http://img2.imgtn.bdimg.com/it/u=2983978887,1448839467&fm=21&gp=0.jpg"'
qq=r.findall(html.text)
# qq=r.findall(te)
# print(te)
# print(html.text)
print(qq)

url = 'http://webapp.fulihui.com/' + qq.pop()
print(url)


# req = requests.get(url)
# print(req.iter_lines(decode_unicode='utf-8'))

# for line in req.iter_lines(decode_unicode='utf-8'):
# 	if line:
# 		print(line)
