#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:26:28 2020

@author: arti
"""

import pandas as pd

df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})

print(df)
print('--')

df2 = df.drop_duplicates()
print(df2)
print('--')

df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)
print('--')