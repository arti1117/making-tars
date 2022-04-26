#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:19:26 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print(df.count())
print('--')
print(type(df.count()))

unique_values = df['origin'].value_counts()
print(unique_values)
print('--')
print(type(unique_values))
