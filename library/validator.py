#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 统一：基本参数验证
import sys as _s


def test(*arguments):  # [list] --根据MongoDB.schema设计
    arv = arguments
    _t = 'type'
    try:
        for x in arv[0].items():  # dict
            # continue if x[0] in arv[1] and isinstance(x[1], arv[1][_t]) else raise ValueError('参数类型错误！')
            if x[0] in arv[1] and isinstance(x[1], arv[1][_t]):
                continue
            else:
                raise ValueError('参数类型错误！')
                break

    except:
        print("Unexpected error:{}".format(_s.exc_info()[0]))
        return False
    else:
        return True
    finally:
        print('------已完成验证------')
