#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:21:43 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.apply(z_score)
print(age_zscore.head())

age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)
print('--')

for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())
        print('--')
        
