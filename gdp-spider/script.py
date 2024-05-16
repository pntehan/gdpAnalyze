#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   script.py
# Time    :   2024/05/16 15:00:59
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


import json, os


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    return data

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)

def genFormatJson(src):
    name = src.split("/")[-1].split(".")[0]
    data = load_json(src)
    # 提取数据节点和维度信息
    datanodes = data['returndata']['datanodes']
    wdnodes = data['returndata']['wdnodes']

    # 提取地区维度信息
    regions = {node['code']:node['cname'] for node in wdnodes[1]['nodes']}
    df = []
    # 遍历数据节点,填充DataFrame
    for node in datanodes:
        if node['data']['hasdata']:
            region = node['wds'][1]['valuecode']
            year = node['wds'][2]['valuecode']
            value = float(node['data']['strdata'])
            df.append({
                "region": regions[region],
                "year": year,
                "value": value,
                "name": name
            })
    save_json(src.replace('data', 'formatData'), df)


if __name__ == "__main__":
    for file_name in os.listdir('data'):
        src = 'data/' + file_name
        genFormatJson(src)

