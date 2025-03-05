#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:54:36 2020

@author: arti
"""

import pandas as pd

df = pd.read_excel('./Stock_Price_Data.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')

df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head(), '\n')

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df.head())
