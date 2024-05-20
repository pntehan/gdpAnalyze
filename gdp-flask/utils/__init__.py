#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   __init__.py
# Time    :   2024/05/20 11:45:33
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from flask import make_response, jsonify


def object2dict(obj):
    d = obj.__dict__
    del d["_sa_instance_state"]
    return d

def json_response(data):
    # 指定返回的数据类型
    response = make_response(jsonify(data))
    response.headers["Content-Type"] = "application/json;charset=UTF-8"
    return response

def extract_year(item):
    year, _ = item.split('-')
    return int(year)
