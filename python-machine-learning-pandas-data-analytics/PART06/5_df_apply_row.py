#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:37:15 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10

def add_two_obj(a, b):
    return a + b

df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)
print(df.head())
print('--')
