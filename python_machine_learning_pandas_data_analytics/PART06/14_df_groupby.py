#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:43:08 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print('승객 수:', len(df))
print('--')

print(df.head())
print('--')

grouped = df.groupby(['class'])
print(grouped)
print('--')

for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('--')
    
average = grouped.mean()
print(average)
print('--')

group3 = grouped.get_group('Third')
print(group3.head())

grouped2 = df.groupby(['class', 'sex'])

for key, group in grouped2:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('--')
    
average2 = grouped2.mean()
print(average2)
print('--')
print(type(average2))

group3f = grouped2.get_group(('Third', 'female'))
print(group3f.head())



