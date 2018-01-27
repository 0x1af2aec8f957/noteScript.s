#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mongodb Config

import sys  ### mac python2.7

sys.path.append('/Library/Python/2.7/site-packages')  ### mac python2.7

from pymongo import MongoClient as m

URL = 'localhost' or '120.0.0.1'  # 地址
PORT = 27017  # 端口
connection = m(URL, PORT)  # 建立连接
db = connection.noteScript  # 连接noteScript数据库，没有则自动创建

__all__ = ['db']  # 仅导出本应用数据库实例
