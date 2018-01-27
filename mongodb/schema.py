#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mongodb Schema
import time  # 时间

USER = lambda: {  # user-table【用户】
    'account': {'type': str},  # 账号
    'gitHub': {'type': str},  # github账号
    'email': {'type': str},  # 邮箱
    'password': {'type': str},  # 密码
    'phone': {'type': int},  # 手机号
    'createDate': {'type': float},  # 创建时间[时间戳]
    'updateDate': {'type': float, 'default': time.time()}  # 最后修改时间
}

LABEL = lambda: {  # label-table【标签】
    'name': {'type': str},  # 名称
    'createDate': {'type': float},  # 创建时间[时间戳]
    'updateDate': {'type': float, 'default': time.time()}  # 最后修改时间
}

COMMENT = lambda: {  # comment-table【评论】
    'article': {'type': str},  # 文章ID
    'content': {'type': str},  # 内容
    'createDate': {'type': float},  # 创建时间[时间戳]
    'updateDate': {'type': float, 'default': time.time()}  # 最后修改时间
}

ARTICLE = lambda: {  # article-table【文章列表】
    'user': {'type': str},  # 作者
    'label': {'type': str},  # label-ID
    'content': {'type': str},  # 内容
    'title': {'type': str},  # 标题
    'createDate': {'type': float},  # 创建时间[时间戳]
    'updateDate': {'type': float, 'default': time.time()}  # 最后修改时间
}
