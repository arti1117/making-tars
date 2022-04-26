#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:00:39 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
font_prop = font_manager.FontProperties(fname=font_path)
plt.rc('font', family=font_name)

plt.style.use('ggplot')
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('The_amount_of_electricity_'+
                   'generated_by_S.Korea_and_N.Korea.xlsx', convert_float=True)
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.T

df = df.rename(columns={'합계':'총발전량'})
df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감률'] = ((df['총발전량']/df['총발전량 - 1년']) - 1 * 100)

ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(20, 10), width=0.7,
                                stacked=True)
ax2 = ax1.twinx()
ax2.plot(df.index, df['증감률'], ls='--', marker='o', markersize=20,
         color='green', label='전년대비 증감률(%)') #안그려짐ㅠㅠ

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20, fontproperties=font_prop)
ax1.set_ylabel('발전량(억 KWh)', fontproperties=font_prop)
ax2.set_ylabel('전년 대비 증감률(%)', fontproperties=font_prop)

plt.title('북한 전력 발전량 (1990-2016)', size=30, fontproperties=font_prop)
ax1.legend(loc='upper left', prop=font_prop)

plt.show()