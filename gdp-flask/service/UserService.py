#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   UserService.py
# Time    :   2024/05/16 16:07:05
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from application import db
from model.User import User
from utils import object2dict, make_response


class UserService:
    def __init__(self):
        pass
    
    def login(self, params):
        # 获取参数
        user_id = params["user_id"]
        password = params["password"]
        # 数据库操作
        user = db.session.query(User).filter(User.id == user_id).first()
        if user.password == password:
            return make_response({"data": object2dict(user), "status": "200"})
        else:
            return make_response({"msg": "帐号或者密码错误", "status": "200"})
    
    def register(self, params):
        # 获取参数
        name = params["name"]
        password = params["password"]
        intro = params["intro"]
        user = User(name, password, intro)
        # 存入数据库
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return make_response({"data": object2dict(user), "status": "200"})
    
    def updateUser(self, params):
        # 获取参数
        user_id = params["id"]
        name = params["name"]
        password = params["password"]
        intro = params["intro"]
        # 先查
        user = db.session.query(User).filter(User.id == user_id).first()
        # 存入数据库
        user.name = name
        user.password = password
        user.intro = intro
        db.session.commit()
        user = db.session.query(User).filter(User.id == user_id).first()
        return make_response({"data": object2dict(user), "status": "200"})
