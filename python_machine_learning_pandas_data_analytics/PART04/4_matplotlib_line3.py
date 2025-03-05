#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:04:06 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = './malgun.ttf'
font_prop = font_manager.FontProperties(fname=font_path)
# plt.rc('font', family=font_prop.get_name())

df = pd.read_excel('Number_of_people_moving_IO_of_cities_and_provinces.xlsx') \
                    .fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')

plt.plot(sr_one.index, sr_one.values)

plt.title('서울 --> 경기도', fontproperties=font_prop)
plt.xlabel('기간', fontproperties=font_prop)
plt.ylabel('이동인구수', fontproperties=font_prop)


plt.legend(labels=['서울 --> 경기'], loc='best')

plt.show()