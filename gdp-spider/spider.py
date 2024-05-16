#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File    :   spider.py
# Time    :   2024/05/16 14:49:19
# Author  :   Pnte Han 
# Version :   1.0
# Contact :   pntehan@gmail.com
# Desc    :   None


import requests, json


response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020101%22%7D%5D&dfwds=%5B%5D&k1=1715843821012")

with open("data/地区生产总值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)


response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020102%22%7D%5D&dfwds=%5B%5D&k1=1715843927579")

with open("data/第一产业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020103%22%7D%5D&dfwds=%5B%5D&k1=1715842483009")

with open("data/第二产业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020104%22%7D%5D&dfwds=%5B%5D&k1=1715842540097")

with open("data/第三产业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020105%22%7D%5D&dfwds=%5B%5D&k1=1715842724555")

with open("data/农林牧渔业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020106%22%7D%5D&dfwds=%5B%5D&k1=1715842739805")

with open("data/工业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020107%22%7D%5D&dfwds=%5B%5D&k1=1715842759888")

with open("data/建筑业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020108%22%7D%5D&dfwds=%5B%5D&k1=1715842774241")

with open("data/批发和零售业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A02010A%22%7D%5D&dfwds=%5B%5D&k1=1715842785296")

with open("data/交通运输和仓储和邮政业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A02010C%22%7D%5D&dfwds=%5B%5D&k1=1715842797855")

with open("data/住宿和餐饮业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)

response = requests.get(r"https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A02010D%22%7D%5D&dfwds=%5B%5D&k1=1715842809752")

with open("data/金融业增加值.json", "w", encoding="utf-8") as fp:
    json.dump(response.json(), fp, indent=4, ensure_ascii=False)
