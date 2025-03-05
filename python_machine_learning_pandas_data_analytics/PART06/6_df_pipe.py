#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:40:15 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'fare']]

def missing_values(x):
    return x.isnull()

def missing_count(x):
    return missing_values(x).sum()

def total_number_missing(x):
    return missing_count(x).sum()

result = df.pipe(missing_values)
print(result.head())
print(type(result))
print('--')

result = df.pipe(missing_count)
print(result)
print(type(result))
print('--')

result = df.pipe(total_number_missing)
print(result)
print(type(result))
print('--')