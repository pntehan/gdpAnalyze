#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   algo_svr.py
# Time    :   2024/05/20 23:17:25
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pickle, joblib
import numpy as np


with open("dataset/train.set", "rb") as fp:
    trainSet = pickle.load(fp)

with open("dataset/test.set", "rb") as fp:
    testSet = pickle.load(fp)


# 将数据转换为 numpy 数组
X = np.array(trainSet["X"])
y_gdp = np.array([row[0] for row in trainSet["Y"]])
y_one = np.array([row[1] for row in trainSet["Y"]])
y_two = np.array([row[2] for row in trainSet["Y"]])
y_three = np.array([row[3] for row in trainSet["Y"]])

# 创建 xgboost 模型
xgb_gdp = xgb.XGBRegressor(max_depth=3, learning_rate=0.0001, n_estimators=1000, objective="reg:squarederror", booster="gbtree", random_state=0)
xgb_one= xgb.XGBRegressor(max_depth=3, learning_rate=0.0001, n_estimators=1000, objective="reg:squarederror", booster="gbtree", random_state=0)
xgb_two = xgb.XGBRegressor(max_depth=3, learning_rate=0.0001, n_estimators=1000, objective="reg:squarederror", booster="gbtree", random_state=0)
xgb_three = xgb.XGBRegressor(max_depth=3, learning_rate=0.0001, n_estimators=1000, objective="reg:squarederror", booster="gbtree", random_state=0)

# 训练 xgboost 模型
xgb_gdp.fit(X, y_gdp)
xgb_one.fit(X, y_one)
xgb_two.fit(X, y_two)
xgb_three.fit(X, y_three)



# 将数据转换为 numpy 数组
X = np.array(testSet["X"])
y_gdp = np.array([row[0] for row in testSet["Y"]])
y_one = np.array([row[1] for row in testSet["Y"]])
y_two = np.array([row[2] for row in testSet["Y"]])
y_three = np.array([row[3] for row in testSet["Y"]])

pred = xgb_gdp.predict(X)
err1 = mean_squared_error(y_gdp, pred)

pred = xgb_one.predict(X)
err2 = mean_squared_error(y_one, pred)

pred = xgb_two.predict(X)
err3 = mean_squared_error(y_two, pred)

pred = xgb_three.predict(X)
err4 = mean_squared_error(y_three, pred)

print("RMSE:", err1, err2, err3, err4)

joblib.dump(xgb_gdp, "xgb_gdp.m")
joblib.dump(xgb_one, "xgb_one.m")
joblib.dump(xgb_two, "xgb_two.m")
joblib.dump(xgb_three, "xgb_three.m")
