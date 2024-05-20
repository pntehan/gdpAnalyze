#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   algo_forest.py
# Time    :   2024/05/20 23:17:25
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from sklearn.ensemble import RandomForestRegressor
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

# 创建随机森林模型
forest_gdp = RandomForestRegressor(n_estimators=100,random_state=0)
forest_one= RandomForestRegressor(n_estimators=100,random_state=0)
forest_two = RandomForestRegressor(n_estimators=100,random_state=0)
forest_three = RandomForestRegressor(n_estimators=100,random_state=0)

# 训练随机森林模型
forest_gdp.fit(X, y_gdp)
forest_one.fit(X, y_one)
forest_two.fit(X, y_two)
forest_three.fit(X, y_three)



# 将数据转换为 numpy 数组
X = np.array(testSet["X"])
y_gdp = np.array([row[0] for row in testSet["Y"]])
y_one = np.array([row[1] for row in testSet["Y"]])
y_two = np.array([row[2] for row in testSet["Y"]])
y_three = np.array([row[3] for row in testSet["Y"]])

pred = forest_gdp.predict(X)
err1 = mean_squared_error(y_gdp, pred)

pred = forest_one.predict(X)
err2 = mean_squared_error(y_one, pred)

pred = forest_two.predict(X)
err3 = mean_squared_error(y_two, pred)

pred = forest_three.predict(X)
err4 = mean_squared_error(y_three, pred)

print("RMSE:", err1, err2, err3, err4)

joblib.dump(forest_gdp, "forest_gdp.m")
joblib.dump(forest_one, "forest_one.m")
joblib.dump(forest_two, "forest_two.m")
joblib.dump(forest_three, "forest_three.m")
