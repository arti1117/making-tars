#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:08:33 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = './malgun.ttf'
font_prop = font_manager.FontProperties(fname=font_path)

df = pd.read_excel('Number_of_people_moving_IO_of_cities_and_provinces.xlsx') \
                    .fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

col_years = list(map(str, range(1970, 2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도', '전라남도'], col_years]
df_4 = df_4.transpose()

plt.style.use('ggplot') 

df_4.index = df_4.index.map(int)

ax = df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))
print(type(ax))

ax.set_title('서울 --> 타시도', size=30, color='brown', weight='bold', 
             fontproperties=font_prop)
ax.set_ylabel('이동 인구수', size=20, color='blue',
              fontproperties=font_prop)
ax.set_xlabel('기간', size=20, color='blue',
              fontproperties=font_prop)
ax.legend(loc='best', fontsize='large', prop=font_prop)

plt.show()