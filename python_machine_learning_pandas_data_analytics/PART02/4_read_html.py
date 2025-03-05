#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 06:29:51 2020

@author: arti
"""

import pandas as pd

url = "https://finance.naver.com/item/main.nhn?code=005380"

tables = pd.read_html(url)

print(len(tables))

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    