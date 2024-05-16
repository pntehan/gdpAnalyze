#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   toMysql.py
# Time    :   2024/05/16 15:43:16
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


import pymysql, json, os


# 连接MySQL数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='gdp_database')


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    return data

def to_db(src):
    data_list = load_json(src)
    with connection.cursor() as cursor:
        for data in data_list:
            print(data)
            sql = "INSERT INTO gdp_data (name, region, year, value) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (data['name'], data['region'], int(data['year']), float(data['value'])))
    # 提交事务
    connection.commit()



if __name__ == "__main__":
    for file_name in os.listdir('formatData'):
        src = 'formatData/' + file_name
        to_db(src)


