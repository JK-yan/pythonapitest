# -*- coding:utf-8 -*-
"""
@version: ??
@author: jackieyan
@license: Apache Licence 
@contact: yanjiankai4618@gmail.com
@site: 
@software: IntelliJ IDEA
@file: GetApi.py
@time: 2016/11/15 16:26
"""
import configparser
import re
import requests


class GetApi(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("D:\CODE\learntest\API_InterfaceTest\Conf\conf.conf")
        self.url = config.get('urls', 'url')
        self.host = config.get('urls', 'host')

    def JS_Adress(self):
        url = self.host + self.url
        """获取页面JS地址"""
        r = re.compile(r'\s*<script src="(js\/.+?\.js)"><\/script>')
        responed = requests.get(url)
        com = r.findall(responed.text)
        responed.close()
        return self.host + com.pop()
        # respond = requests.get(url=aa, stream=True)
        # for line in respond.iter_lines(decode_unicode="utf-8"):
        #     if line:
        #         com = r.findall(line)
        #         if com:
        #             # print(self.host + com.pop())
        #             return self.host + com.pop()

    def get_api(self):
        url = self.JS_Adress()
        respond = requests.get(url)
        respond.close()
        print(respond.text)
        # for line in respond.iter_lines(decode_unicode="utf-8"):
        #     if line:
        #         print(line)
        # print(respond.text)
        # return respond.status_code


if __name__ == '__main__':
    GetApi().get_api()
    # print(GetApi.JS_Adress())JS_Adress
    # print(selfJS_Adress())
