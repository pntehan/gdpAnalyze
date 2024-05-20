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
from utils import object2dict, make_response, extract_year
import joblib
import numpy as np


class DataServcie:
    def __init__(self):
        self.region_list = [
            "青海省", "四川省", "甘肃省", "宁夏回族自治区", "内蒙古自治区", "山西省", "陕西省", "河南省", "山东省"
        ]
        self.name_list = ["地区生产总值", "第一产业增加值", "第二产业增加值", "第三产业增加值"]
        self.algo_svr = [joblib.load("static/svr_gdp.m"), joblib.load("static/svr_one.m"), joblib.load("static/svr_two.m"), joblib.load("static/svr_three.m")]
        self.algo_xgb = [joblib.load("static/xgb_gdp.m"), joblib.load("static/xgb_one.m"), joblib.load("static/xgb_two.m"), joblib.load("static/xgb_three.m")]
        self.algo_forest = [joblib.load("static/forest_gdp.m"), joblib.load("static/forest_one.m"), joblib.load("static/forest_two.m"), joblib.load("static/forest_three.m")]
    
    def getGDPData(self):
        gdp_list = db.session.query(GdpData).all()
        return make_response([object2dict(gdp) for gdp in gdp_list if gdp.region in self.region_list])

    def predict(self, params):
        import random
        # 获取参数
        region = params["region"]
        algo = params["algo"]
        # 输入数据准备
        data = []
        for name in self.name_list:
            gdp_list = db.session.query(GdpData).filter(GdpData.region == region, GdpData.name == name).order_by(GdpData.year).all()
            data.append([])
            data[-1] = [x.value for x in gdp_list]
        data = np.transpose(np.array(data))
        # 特征制作
        x = (data[-1] - data[0]) / data[0]
        if algo == "svr":
            pred = [
                {"region": region, "name": "地区生产总值", "value": 0},
                {"region": region, "name": "第一产业增加值", "value": 0},
                {"region": region, "name": "第二产业增加值", "value": 0},
                {"region": region, "name": "第三产业增加值", "value": 0}
            ]
            for i, algo in enumerate(self.algo_svr):
                y = algo.predict([x])[0]
                # 解码
                pred[i]["value"] = y * data[-1][i] + data[-1][i]
        elif algo == "xgb":
            pred = [
                {"region": region, "name": "地区生产总值", "value": 0},
                {"region": region, "name": "第一产业增加值", "value": 0},
                {"region": region, "name": "第二产业增加值", "value": 0},
                {"region": region, "name": "第三产业增加值", "value": 0}
            ]
            for i, algo in enumerate(self.algo_xgb):
                y = algo.predict([x])[0]
                # 解码
                pred[i]["value"] = y * data[-1][i] + data[-1][i]
        elif algo == "forest":
            pred = [
                {"region": region, "name": "地区生产总值", "value": 0},
                {"region": region, "name": "第一产业增加值", "value": 0},
                {"region": region, "name": "第二产业增加值", "value": 0},
                {"region": region, "name": "第三产业增加值", "value": 0}
            ]
            for i, algo in enumerate(self.algo_forest):
                y = algo.predict([x])[0]
                # 解码
                pred[i]["value"] = y * data[-1][i] + data[-1][i]
        return make_response(pred)
