#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:22:42 2020

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

col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도', '전라남도'], col_years]
df_4['합계'] = df_4.sum(axis=1)

df_total = df_4[['합계']].sort_values(by='합계', ascending=True)
df_total = df_total.rename(index={'충청남도':'Chungnam', '경상북도':'Gyeongbuk',
                                  '강원도':'Gangwon', '전라남도':'Jeonnam'})

plt.style.use('ggplot')

df_total.plot(kind='barh', color='cornflowerblue', width=0.7,
              figsize=(10, 5))

plt.yticks(
           fontproperties=font_prop,
           fontsize=15,
           )

plt.title('서울 --> 타시도', size=30, fontproperties=font_prop)
plt.ylabel('전입지', size=20, fontproperties=font_prop)
plt.xlabel('이동 인구 수', size=20, fontproperties=font_prop)
plt.legend(loc='best', prop=font_prop)

plt.show()