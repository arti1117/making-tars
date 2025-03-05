#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 06:33:07 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')
df = titanic.loc[:, ['age', 'fare']]

def min_max(x):
    return x.max() - x.min()

result = df.apply(min_max)
print(result)
print('--')
print(type(result))
