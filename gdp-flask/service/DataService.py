#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   DataService.py
# Time    :   2024/05/16 16:07:19
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from application import db
from model.GdpData import GdpData
from utils import object2dict, make_response


class DataServcie:
    def __init__(self):
        self.region_list = [
            "青海省", "四川省", "甘肃省", "宁夏回族自治区", "内蒙古自治区", "山西省", "陕西省", "河南省", "山东省"
        ]
    
    def getGDPData(self):
        gdp_list = db.session.query(GdpData).all()
        return make_response([object2dict(gdp) for gdp in gdp_list if gdp.region in self.region_list])