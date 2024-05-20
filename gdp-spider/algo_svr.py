#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   algo_svr.py
# Time    :   2024/05/20 23:17:25
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


from sklearn.svm import SVR
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

# 创建 SVR 模型
svr_gdp = SVR(kernel="rbf")
svr_one= SVR(kernel="rbf")
svr_two = SVR(kernel="rbf")
svr_three = SVR(kernel="rbf")

# 训练 SVR 模型
svr_gdp.fit(X, y_gdp)
svr_one.fit(X, y_one)
svr_two.fit(X, y_two)
svr_three.fit(X, y_three)



# 将数据转换为 numpy 数组
X = np.array(testSet["X"])
y_gdp = np.array([row[0] for row in testSet["Y"]])
y_one = np.array([row[1] for row in testSet["Y"]])
y_two = np.array([row[2] for row in testSet["Y"]])
y_three = np.array([row[3] for row in testSet["Y"]])

pred = svr_gdp.predict(X)
err1 = mean_squared_error(y_gdp, pred)

pred = svr_one.predict(X)
err2 = mean_squared_error(y_one, pred)

pred = svr_two.predict(X)
err3 = mean_squared_error(y_two, pred)

pred = svr_three.predict(X)
err4 = mean_squared_error(y_three, pred)

print("RMSE:", err1, err2, err3, err4)

joblib.dump(svr_gdp, "svr_gdp.m")
joblib.dump(svr_one, "svr_one.m")
joblib.dump(svr_two, "svr_two.m")
joblib.dump(svr_three, "svr_three.m")
