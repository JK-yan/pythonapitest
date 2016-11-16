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

r = re.compile(r'<script src="(js\/.+?\.js)"><\/script>')
qq=r.findall('<script src="js/main-min-5dcb9d010f.js"></script>')
print(qq)

url = 'http://webapp.fulihui.com/' + qq
print(url)


req = requests.get(url)
print(req.iter_lines(decode_unicode='utf-8'))

# for line in req.iter_lines(decode_unicode='utf-8'):
# 	if line:
# 		print(line)
