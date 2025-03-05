#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:53:59 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Number_of_people_moving_IO_of_cities_and_provinces.xlsx') \
                    .fillna(method='ffill')

print(df.head())
print('--')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

print(df_seoul.head())
print('--')

sr_one = df_seoul.loc['경기도']
print(sr_one.head())
print('--')

#plt.plot(sr_one.index, sr_one.values)
plt.plot(sr_one)