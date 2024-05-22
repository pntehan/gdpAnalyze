#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   DataController.py
# Time    :   2024/05/16 16:05:40
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from flask import Blueprint, request
from service.DataService import DataServcie


# 创建数据蓝图
DataRouter = Blueprint("DataRouter", __name__, url_prefix="/data")
# 创建服务对象
data_service = DataServcie()


@DataRouter.route("/getGDPData", methods=["GET"])
def getGDPData():
    return data_service.getGDPData()

@DataRouter.route("/addGDPData", methods=["POST"])
def addGDPData():
    params = request.json
    return data_service.addGDPData(params)

@DataRouter.route("/editGDPData", methods=["POST"])
def editGDPData():
    params = request.json
    return data_service.editGDPData(params)

@DataRouter.route("/deleteGDPData", methods=["POST"])
def deleteGDPData():
    params = request.json
    return data_service.deleteGDPData(params)

@DataRouter.route("/predict", methods=["POST"])
def predict():
    params = request.json
    return data_service.predict(params)
