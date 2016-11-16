# -*- coding:utf-8 -*-
"""
@version: ??
@author: jackieyan
@license: Apache Licence 
@contact: yanjiankai4618@gmail.com
@site: 
@software: IntelliJ IDEA
@file: TimesUtil.py
@time: 2016/11/15 16:14
"""
import time


def get_time():
    """获取当前日期时间"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))