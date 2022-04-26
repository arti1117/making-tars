#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 07:28:39 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./titanic.csv')

print(df.head())
print('--')
print(df.info())
print('--')

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)
print('--')
print(df.head().isnull())
print('--')
print(df.head().notnull())
print('--')
print(df.head().isnull().sum(axis=0))