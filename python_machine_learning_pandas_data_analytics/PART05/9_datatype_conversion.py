#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:38:34 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print(df.dtypes)
print('--')

print(df['horsepower'].unique())
print('--')

import numpy as np

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df['horsepower'].dtypes)
print('--')

print(df['origin'].unique())
print('--')

df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)

print(df['origin'].unique())
print(df['origin'].dtypes)
print('--')

df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)
print('--')

df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)
print('--')

print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))

