#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:48:45 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

age_mean = grouped.age.mean()
print(age_mean)
print('--')

age_std = grouped.age.std()
print(age_std)
print('--')

for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head(3))
    print('--')
    
def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]])
print('--')

print(len(age_zscore))
print('--')

print(age_zscore.loc[0:9])
print('--')

print(type(age_zscore))            