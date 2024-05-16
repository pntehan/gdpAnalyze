#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   GdpData.py
# Time    :   2024/05/16 16:02:38
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from application import db


class GdpData(db.Model):
    __tablename__ = "gdp_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    region = db.Column(db.String(255))
    year = db.Column(db.Integer)
    value = db.Column(db.Float)

    def __init__(self, name, region, year, value):
        self.name = name
        self.region = region
        self.year = year
        self.value = value
