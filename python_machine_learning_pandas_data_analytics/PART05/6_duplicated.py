#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:19:00 2020

@author: arti
"""

import pandas as pd

df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})

print(df)
print('--')

df_dup = df.duplicated()
print(df_dup)
print('--')

col_dup = df['c2'].duplicated()
print(col_dup)