# -*- coding:utf-8 -*-
"""
@version: ??
@author: jackieyan
@license: Apache Licence 
@contact: yanjiankai4618@gmail.com
@site: 
@software: IntelliJ IDEA
@file: Demo1.py
@time: 2016/11/14 14:17
"""
import requests
import re

req = requests.get('http://www.baidu.com')
print(req.json())


def __get_html(self):
    """
	获得指定url的html
	:return: 返回一个byte流html
	"""
    # return urllib.request.urlopen(self.Url).read()
    return requests.get().iter_content()


def __get_api(self):
    """
	通过正则表达式匹配相应的接口
	:return: 返回一个匹配后的接口列表
	"""
    html = self.__get_html()
    html
    print("接口拉取成功")
    reg = re.compile(r'<a href="(.+?)" title="(.+?)">(.+?)</a>')
    return re.findall(reg, html)
