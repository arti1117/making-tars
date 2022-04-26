#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:23:08 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = './malgun.ttf'
font_prop = font_manager.FontProperties(fname=font_path)

df = pd.read_excel('Number_of_people_moving_IO_of_cities_and_provinces.xlsx') \
                    .fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

fig = plt.figure(figsize=(20, 5))

ax = fig.add_subplot(1, 1, 1)

ax.plot(sr_one, marker='o', markerfacecolor='orange', markersize=10,
         color='olive', linewidth=2, label='Seoul --> Gyeonggi')
ax.legend(loc='best')

ax.set_title('Seoul --> Gyeonggi', size=20)

ax.set_xlabel('기간',size=12, fontproperties=font_prop)
ax.set_xlabel('이동인구수',size=12, fontproperties=font_prop)

ax.set_ylim(50000, 800000)

idx = sr_one.index.tolist()

ax.set_xticklabels(idx, rotation=75)

ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis='y', labelsize=10)

plt.show()
