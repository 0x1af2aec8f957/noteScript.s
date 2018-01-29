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
        if (not _v.test(dict, _s[self.__class__.__name__]())):  # TODO:多条插入需要逐步循环验证
            raise ValueError('{}：参数类型错误'.format(name))
        self.data = dict
        # print(self.__class__.__name__)
        self.db = db[self.__class__.__name__]  # 使用user集合，没有则自动创建
        return

    def insert(self, dict):  # 插入
        # self.db.save(self.data)
        return self.db.insert(dict)

    def findOne(self, dict):  # 单个查找
        return self.db.find_one(dict)

    def find(self, dict, skip=1 * 15, limit=15):  # 查询
        return self.db.find(dict).skip(skip).limit(limit)

    def remove(self, dict):  # 移除
        return self.db.remove(dict)

    def update(self, dict, data):  # 修改
        return self.db.update(dict, data)


# user()


class label:  # 文章标签/分类
    def __init__(self, dict):
        self.data = dict
        self.db = db[self.__class__.__name__]  # 使用label集合，没有则自动创建

    def insert(self, dict):  # 插入
        # self.db.save(self.data)
        return self.db.insert(dict)

    def findOne(self, dict):  # 单个查找
        return self.db.find_one(dict)

    def find(self, dict, skip=1 * 15, limit=15):  # 查询
        return self.db.find(dict).skip(skip).limit(limit)

    def remove(self, dict):  # 移除
        return self.db.remove(dict)

    def update(self, dict, data):  # 修改
        return self.db.update(dict, data)


class commet:  # 文章评论
    def __init__(self, dict):
        self.data = dict
        self.db = db[self.__class__.__name__]  # 使用commet集合，没有则自动创建

    def insert(self, dict):  # 插入
        # self.db.save(self.data)
        return self.db.insert(dict)

    def findOne(self, dict):  # 单个查找
        return self.db.find_one(dict)

    def find(self, dict, skip=1 * 15, limit=15):  # 查询
        return self.db.find(dict).skip(skip).limit(limit)

    def remove(self, dict):  # 移除
        return self.db.remove(dict)

    def update(self, dict, data):  # 修改
        return self.db.update(dict, data)


class article:  # 文章列表
    def __init__(self, dict):
        self.data = dict
        self.db = db[self.__class__.__name__]  # 使用article集合，没有则自动创建

    def insert(self, dict):  # 插入
        # self.db.save(self.data)
        return self.db.insert(dict)

    def findOne(self, dict):  # 单个查找
        return self.db.find_one(dict)

    def find(self, dict, skip=1 * 15, limit=15):  # 查询
        return self.db.find(dict).skip(skip).limit(limit)

    def remove(self, dict):  # 移除
        return self.db.remove(dict)

    def update(self, dict, data):  # 修改
        return self.db.update(dict, data)
