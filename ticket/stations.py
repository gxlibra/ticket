#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9092'

# 下载数据,无需验证证书
response = requests.get(url, verify=False)

# 正则匹配中文和大写字码
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)

# 优雅打印
pprint(dict(stations), indent=4)

# 写入文件中
# s = dict(stations)
# # with open('stations.py','w',encoding='utf-8') as f:
# #     f.write(str(s))