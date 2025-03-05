#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:46:08 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:4, 'survived':'age']
print(df.head(), '\n')

columns = list(df.columns.values)
print(columns, '\n')

sorted_columns = sorted(columns)
df_sorted = df[sorted_columns]
print(df_sorted, '\n')

reversed_columns = list(reversed(columns))
df_reversed = df[reversed_columns]
print(df_reversed, '\n')

customed_columns = ['pclass', 'age', 'sex', 'survived']
df_customed = df[customed_columns]
print(df_customed, '\n')
