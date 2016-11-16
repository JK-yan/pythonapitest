# -*- coding:utf-8 -*-
"""
@version: ??
@author: jackieyan
@license: Apache Licence
@contact: yanjiankai4618@gmail.com
@site:
@software: IntelliJ IDEA
@file: Demo4.py
@time: 2016/11/15 13:45
"""
import re

import requests


def req(url):
    responed = requests.get(url)
    r = re.compile(r'<script src="(js\/.+?\.js)"><\/script>')
    com = r.findall(responed.text)
    print(com.pop())
    # for i in responed.text:
    #     com = r.findall(i)
    #     print(com)

    # diedai = responed.iter_lines(decode_unicode="utf-8")
    # for line in diedai:

    #     # print(line)
    #     r = re.compile(r'\s*<script src="(js\/.+?\.js)"><\/script>')
    #     # com = r.findall(line)
    #     # print(com)
    #     if line:
    #         # r = re.compile(r'<script src="(js\/.+?\.js)"><\/script>', re.X)
    #         com = r.findall(line)
    #         # print(com)
    #         print('……………………………………………………………………分割线………………………………………………………………………………')
    #         # print(r.findall(line).pop())
    #         if com:
    #             print(234224232323)
    #             print(com.pop())
    #         # print(line)
    #         # return line
    #         # return requests.request(method, url).iter_lines(decode_unicode="utf-8")


def get_js(html=''):
    # html = req()
    r = re.compile(r'<script src="(js\/.+?\.js)"><\/script>', re.X)
    if r.findall(html):
        return r.findall(html).pop()


if __name__ == '__main__':
    # print(req(url='http://webapp.fulihui.com/home/index/'))
    req(url='http://webapp.fulihui.com/home/index/')

# print(get_js(html=req(url='http://webapp.fulihui.com/home/index/')))
