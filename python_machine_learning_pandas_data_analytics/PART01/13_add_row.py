#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 06:26:32 2020

@author: arti
"""

import pandas as pd

exam_data = {'Name': ['Sep', 'Jul', 'Aug'],
             'Math': [90, 80, 70],
             'English': [89, 99, 50],
             'Music': [50, 70, 100],
             'Sports': [70, 30, 100]}

df = pd.DataFrame(exam_data)
print(df); print('---')

df.loc[3] = 0
print(df); print('---')

df.loc[5] = -1
print(df); print('---')

df.loc[6] = ['Oct', 10, 10, 100, 100]
print(df); print('---')

df.loc['No7'] = df.loc[3]
print(df); print('---')
