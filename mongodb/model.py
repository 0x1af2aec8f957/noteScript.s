#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mongodb Model

# import sys
from config import *  # db --MongoDB数据库实例
import schema as _s  # mongodb Schema

# sys.path.append("..")  # 增加上层‘‘模块’’目录
from library import validator as _v  # 进行参数验证

print(_v['test'])


class user:  # 用户
    def __init__(self, dict={}):
        name = self.__class__.__name__
        if (not _v.test(dict, _s[name]())):
            raise ValueError('{}：参数类型错误'.format(name))
        self.data = dict
        # print(self.__class__.__name__)
        self.db = db.name  # 使用user集合，没有则自动创建

    def insert(self):  # 插入
        pass

    def findOne(self):  # 单个查找
        pass

    def find(self):  # 查询
        pass

    def remove(self):  # 移除
        pass

    def update(self):  # 修改
        pass


# user()


class label:  # 文章标签/分类
    def __init__(self, dict):
        self.data = dict
        self.db = db[self.__class__.__name__]  # 使用label集合，没有则自动创建

    def insert(self):  # 插入
        pass

    def findOne(self):  # 单个查找
        pass

    def find(self):  # 查询
        pass

    def remove(self):  # 移除
        pass

    def update(self):  # 修改
        pass


class commet:  # 文章评论
    def __init__(self, dict):
        self.data = dict
        self.db = db[self.__class__.__name__]  # 使用commet集合，没有则自动创建

    def insert(self):  # 插入
        pass

    def findOne(self):  # 单个查找
        pass

    def find(self):  # 查询
        pass

    def remove(self):  # 移除
        pass

    def update(self):  # 修改
        pass


class article:  # 文章列表
    def __init__(self, dict):
        self.data = dict
        self.db = db[self.__class__.__name__]  # 使用article集合，没有则自动创建

    def insert(self):  # 插入
        pass

    def findOne(self):  # 单个查找
        pass

    def find(self):  # 查询
        pass

    def remove(self):  # 移除
        pass

    def update(self):  # 修改
        pass
