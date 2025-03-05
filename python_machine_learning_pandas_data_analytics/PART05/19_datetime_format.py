#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:31:16 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('stock-data.csv')

df['new_Date'] = pd.to_datetime(df.Date)
print(df.head())
print('--')

df['Year'] = df.new_Date.dt.year
df['Month'] = df.new_Date.dt.month
df['Day'] = df.new_Date.dt.day
print(df.head())
print('--')

df['Date_yr'] = df.new_Date.dt.to_period(freq='A')
df['Date_m'] = df.new_Date.dt.to_period(freq='M')
print(df.head())
print('--')

df.set_index('Date_m', inplace=True)
print(df.head())
