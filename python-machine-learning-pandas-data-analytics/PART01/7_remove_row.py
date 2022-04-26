#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 05:24:49 2020

@author: arti
"""

import pandas as pd

exam_data = {'Math': [90, 80, 70], 'English': [89, 99, 50],
             'Music': [50, 70, 100], 'Sports': [70, 30, 100]}

df = pd.DataFrame(exam_data, index=['Sep', 'Jul', 'Aug'])

print(df)
print('-----------')

df2 = df[:].copy()
print(df2)
print('-----------')

df2.drop('Sep', inplace=True)
# print(df)
# print('-----------')
print(df2)
print('-----------')

df3 = df[:].copy()
df3.drop(['Sep', 'Aug'], axis=0, inplace=True)
print(df3)