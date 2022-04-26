#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:09:05 2020

@author: arti
"""

import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)
print('--')

bin_names = ['Low', 'Normal', 'High']

df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_dividers,
                      labels=bin_names,
                      include_lowest=True)

horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))