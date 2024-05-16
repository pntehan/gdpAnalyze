#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   application.py
# Time    :   2024/05/16 15:58:18
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config


# Flask程序生成
app = Flask(__name__)
app.config.from_object(config)
# 数据库初始化app
db = SQLAlchemy(app)


# 加载路由
from controller import *
