#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:40:13 2020

@author: arti
"""

import pandas as pd

list_data = ['2020-08-04', 3.14, 'ABC', 2.7818, True]

print(type(list_data))

sr = pd.Series(list_data)

print(sr)
print(sr[1])

idx = sr.index
val = sr.values

print(idx)

print('\n')

print(val)