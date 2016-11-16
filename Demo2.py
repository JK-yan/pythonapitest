# -*- coding:utf-8 -*-
"""
@version: ??
@author: jackieyan
@license: Apache Licence 
@contact: yanjiankai4618@gmail.com
@site: 
@software: IntelliJ IDEA
@file: Demo2.py
@time: 2016/11/14 15:22
"""


import requests
import configparser

config = configparser.ConfigParser()
rets = config.read("E:\Code\learntest\API_InterfaceTest\Conf\conf.conf")

w = config.get('urls', 'host')
e = config.get('urls', 'url')
print (w+e)
a = 'http://httpbin.org/stream/20'
c = 'http://webapp.fulihui.com/home/index/'
jsons = {
    'headers': {
        'Content-Encoding ': 'utf-8'
    }
}
hearder = {'Content-Encoding ': 'utf-8'}
r = requests.get(c, headers=hearder, stream=True)
d = r.iter_lines(decode_unicode="utf-8")

print(r.text)
print(r.headers)


# for line in r:
# 	print(line.decode('utf-8'))
# print(r.iter_content(decode_unicode='utf-8'))
# for line in d:
#     # print(line.decode('utf-8'))
#     # b = line.decode('utf-8')
#
#     # filter out keep-alive new lines
#     if line:
#         print(json.loads(line))
#         print('……………………………………………………………………分割线………………………………………………………………………………')
    # print(json.loads(line))

# for line in r.iter_content(decode_unicode=True):
# 	# print(line.decode('utf-8'))
# 	# li
#
# 	# filter out keep-alive new lines
# 	if line:
# 		print(line)
