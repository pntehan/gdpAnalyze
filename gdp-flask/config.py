#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   config.py
# Time    :   2024/05/16 15:56:32
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


import os

# base config
SECRET_KEY = os.urandom(32)
BASE_DIR   = os.path.abspath(os.path.dirname(__file__))
DEBUG      = False
HOST       = "127.0.0.1"
JSON_AS_ASCII = False
# database config
SQLALCHEMY_DATABASE_URI = "mysql://root:^Zh123528@127.0.0.1:3306/gdp_database"
# SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/gdp_database"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_PRE_PING = True
SQLALCHEMY_POOL_RECYCLE = 7200
SQLALCHEMY_POOL_TIMEOUT = 900
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 10
