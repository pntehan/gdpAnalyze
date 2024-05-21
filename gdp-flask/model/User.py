#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   User.py
# Time    :   2024/05/21 12:00:29
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from application import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    intro = db.Column(db.String(255))

    def __init__(self, name, password, intro):
        self.name = name
        self.password = password
        self.intro = intro
