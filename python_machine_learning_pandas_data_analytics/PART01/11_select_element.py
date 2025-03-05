#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 06:01:45 2020

@author: arti
"""

import pandas as pd

exam_data = {'Name': ['Sep', 'Jul', 'Aug'],
             'Math': [90, 80, 70],
             'English': [89, 99, 50],
             'Music': [50, 70, 100],
             'Sports': [70, 30, 100]}

df = pd.DataFrame(exam_data)

df.set_index('Name', inplace=True)

print(df)
print('------')

a = df.loc['Sep', 'English']
print(a)
print('-----')

b = df.iloc[0, 1]
print(b)
print('-----')

c = df.loc['Sep', ['Music', 'Sports']]
print(c)
print('-----')

d = df.iloc[0, [2, 3]]
print(d)
print('-----')

e = df.loc['Sep', 'Music':'Sports']
print(e)
print('-----')

f = df.iloc[0, 2:4]
print(f)
print('-----')

g = df.loc[['Jul', 'Aug'], ['English', 'Music']]
print(g)
print('-----')

h = df.iloc[[1, 2], [1, 2]]
print(h)
print('-----')

i = df.loc['Sep':'Jul', 'Math':'English']
print(i)
print('-----')

j = df.iloc[0:2, 0:2]
print(j)
print('-----')