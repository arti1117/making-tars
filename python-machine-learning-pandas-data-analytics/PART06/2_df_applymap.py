#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:20:54 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('--')

def add_10(n):
    return n + 10


df_map = df.applymap(add_10)
print(df_map.head())
print('--')
