#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:29:27 2020

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

plt.style.use('ggplot')

plt.figure(figsize=(14, 5))
plt.xticks(size=10, rotation='vertical')

plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

plt.title('서울 --> 경기도', fontproperties=font_prop, size=30)
plt.xlabel('기간', fontproperties=font_prop, size=20)
plt.ylabel('이동인구수', fontproperties=font_prop, size=20)


plt.legend(labels=['Seoul --> Gyenggi'], loc='best', fontsize=15)

plt.ylim(50000, 800000)

plt.annotate('',
             xy=(20, 620000),
             xytext=(2, 290000),
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5),
             )

plt.annotate('',
             xy=(47, 450000),
             xytext=(30, 580000),
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),
             )

plt.annotate('인구 이동 증가(1970-1995)',
             xy=(10, 400000),
             rotation=25,
             va='baseline',
             ha='center',
             fontsize=15,
             fontproperties=font_prop,
             )

plt.annotate('인구 이동 감소(1955-2017)',
             xy=(39, 510000),
             rotation=-11,
             va='baseline',
             ha='center',
             fontsize=15,
             fontproperties=font_prop,
             )

plt.show()