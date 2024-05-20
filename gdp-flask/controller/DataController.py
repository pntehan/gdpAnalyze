#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   DataController.py
# Time    :   2024/05/16 16:05:40
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from flask import Blueprint
from service.DataService import DataServcie


# 创建数据蓝图
DataRouter = Blueprint("DataRouter", __name__, url_prefix="/data")
# 创建服务对象
data_service = DataServcie()


@DataRouter.route("/getGDPData", methods=["GET"])
def getGDPData():
    return data_service.getGDPData()
