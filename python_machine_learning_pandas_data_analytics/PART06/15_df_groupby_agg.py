#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:24:09 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all)
print('--')

print(type(std_all))
print('--')

std_fare = grouped.fare.std()
print(std_fare)
print('--')

print(type(std_fare))
print('--')

def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())
print('--')

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print('--')

agg_sep = grouped.agg({'fare': ['min', 'max'], 'age':'mean'})
print(agg_sep.head())
print('--')


