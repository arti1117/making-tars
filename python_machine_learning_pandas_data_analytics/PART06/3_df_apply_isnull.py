#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:24:28 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('--')

def missing_values(series):
    return series.isnull()

result = df.apply(missing_values, axis=0)
print(result.head())
print('--')

print(type(result))
