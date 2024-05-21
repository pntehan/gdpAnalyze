#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   UserController.py
# Time    :   2024/05/16 16:04:22
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from flask import Blueprint, request
from service.UserService import UserService

# 创建用户蓝图
UserRouter = Blueprint("UserRouter", __name__, url_prefix="/user")

# 创建服务对象
user_service = UserService()


@UserRouter.route("/login", methods=["POST"])
def login():
    params = request.json
    return user_service.login(params)

@UserRouter.route("/register", methods=["POST"])
def register():
    params = request.json
    return user_service.register(params)

@UserRouter.route("/updateUser", methods=["POST"])
def updateUser():
    params = request.json
    return user_service.updateUser(params)
