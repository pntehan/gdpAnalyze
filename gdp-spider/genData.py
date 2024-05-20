#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   genData.py
# Time    :   2024/05/20 22:31:51
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


import json, pickle
import numpy as np


def extract_year(item):
    year, _ = item.split('-')
    return int(year)


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    data_list = [x for x in data if x["region"] in region_list]
    data = {}
    for item in data_list:
        if item["region"] not in data:
            data[item["region"]] = []
        data[item["region"]].append(item["year"]+"-"+str(item["value"]))
    for k in data:
        t = sorted(data[k], key=extract_year)
        data[k] = [float(x.split("-")[-1]) for x in t]
    return data

def merge_data(gdp_data, one_data, two_data, three_data):
    data = {}
    for region in region_list:
        data[region] = []
        for i in range(9):
            data[region].append([gdp_data[region][i], one_data[region][i], two_data[region][i], three_data[region][i]])
    return data

def create_trainSet(data):
    X_set = []
    Y_set = []
    for region in data.keys():
        if region not in train_list:
            continue
        # 开始创建
        data_list = data[region]
        for i in range(4, 8):
            x = np.array(data_list[0:i])
            # 进行平均期望求解
            x = (x[-1] - x[0]) / x[0]
            y = (np.array(data_list[i+1]) - np.array(data_list[i])) / np.array(data_list[i])
            X_set.append(x)
            Y_set.append(y)
    trainSet = {"X": X_set, "Y": Y_set}
    with open("dataset/train.set", "wb") as fp:
        pickle.dump(trainSet, fp)

def create_testSet(data):
    X_set = []
    Y_set = []
    for region in data.keys():
        if region not in test_list:
            continue
        # 开始创建
        data_list = data[region]
        for i in range(4, 8):
            x = np.array(data_list[0:i])
            # 进行平均期望求解
            x = (x[-1] - x[0]) / x[0]
            y = (np.array(data_list[i+1]) - np.array(data_list[i])) / np.array(data_list[i])
            X_set.append(x)
            Y_set.append(y)
    testSet = {"X": X_set, "Y": Y_set}
    with open("dataset/test.set", "wb") as fp:
        pickle.dump(testSet, fp)


region_list = [
    "青海省", "四川省", "甘肃省", "宁夏回族自治区", "内蒙古自治区", "山西省", "陕西省", "河南省", "山东省"
]

train_list = [
    "青海省", "四川省", "甘肃省", "宁夏回族自治区", "内蒙古自治区", "山西省"
]

test_list = [
    "陕西省", "河南省", "山东省"
]

gdp_data = load_json("formatData/地区生产总值.json")
one_data = load_json("formatData/第一产业增加值.json")
two_data = load_json("formatData/第二产业增加值.json")
three_data = load_json("formatData/第三产业增加值.json")

data = merge_data(gdp_data, one_data, two_data, three_data)
create_trainSet(data)
create_testSet(data)
