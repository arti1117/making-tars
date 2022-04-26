#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 09:07:22 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Number_of_people_moving_IO_of_cities_and_provinces.xlsx') \
                    .fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

plt.plot(sr_one.index, sr_one.values)
plt.title('Seoul --> Gyeonggi-do')
plt.xlabel('Periods')
plt.ylabel('Moving Population')
plt.show()
