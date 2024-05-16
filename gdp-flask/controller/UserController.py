#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   UserController.py
# Time    :   2024/05/16 16:04:22
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from flask import Blueprint

# 创建用户蓝图
UserRouter = Blueprint("UserRouter", __name__, url_prefix="/user")
