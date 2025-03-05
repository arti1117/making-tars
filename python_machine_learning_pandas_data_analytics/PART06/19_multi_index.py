#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:32:22 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class', 'sex'])

gdf = grouped.mean()
print(gdf)
print('--')
print(type(gdf))

print(gdf.loc['First'])
print('--')

print(gdf.loc[('First', 'female')])
print('--')

print(gdf.xs('male', level='sex'))
print('--')