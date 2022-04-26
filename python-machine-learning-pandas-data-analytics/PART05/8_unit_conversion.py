#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:29:01 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print(df.head(3))
print('--')

mpg_to_kpl = 1.60394 / 3.78541

df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3))
print('--')

df['kpl'] = df['kpl'].round(2)
print(df.head(3))