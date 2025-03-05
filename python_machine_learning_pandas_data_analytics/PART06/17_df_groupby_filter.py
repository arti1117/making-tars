#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:06:26 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head())
print('--')
print(type(grouped_filter))

age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.tail())
print('--')
print(type(age_filter))

age_grouped = grouped.apply(lambda x: x.describe())
print(age_grouped)
print('--')

