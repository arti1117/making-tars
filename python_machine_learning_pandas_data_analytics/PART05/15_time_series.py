#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:05:50 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('stock-data.csv')

print(df.head())
print('--')
print(df.info())

df['new_Date'] = pd.to_datetime(df.Date)

print(df.head())
print('--')
print(df.info())
print('--')
print(type(df['new_Date'][0]))
print('--')

df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)

print(df.head())
print('--')
print(df.info())
