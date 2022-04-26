#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:12:26 2020

@author: arti
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing as pre

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(count)
print(bin_dividers)

bin_names = ['Low', 'Normal', 'High']
# [1, 2, 0]

df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_dividers,
                      labels=bin_names,
                      include_lowest=True)

horsepower_dummies = pd.get_dummies(df['hp_bin'])

label_encoder = pre.LabelEncoder()
onehot_encoder = pre.OneHotEncoder()

onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))
print('--')

onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshaped)
print(type(onehot_reshaped))
print('--')

onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))

print(df['hp_bin'].head(15))
