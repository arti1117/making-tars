#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 06:08:12 2020

@author: arti
"""

import pandas as pd

file_path = './GeneratedEnergy.xlsx'

df1 = pd.read_excel(file_path)
df2 = pd.read_excel(file_path, header=1)

print(df1)
print(df2)