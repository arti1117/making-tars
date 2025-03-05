#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 19:30:05 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "./malgun.ttf"
font_prop = font_manager.FontProperties(fname=font_path)
font_name = font_prop.get_name()
rc('font', family=font_name)

plt.style.use('seaborn-poster')
plt.rcParams['axes.unicode_minus']=False

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA', 'EU', 'JPN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA', 'EU', 'JPN'],
               vert=False)

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)', fontproperties=font_prop)
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)', fontproperties=font_prop)

plt.show()
