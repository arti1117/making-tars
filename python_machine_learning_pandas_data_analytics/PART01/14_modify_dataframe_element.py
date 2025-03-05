#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 06:30:48 2020

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
print(df); print('--')

df.iloc[0][3] = 80
print(df); print('--')

df.loc['Jul']['Music'] = 100
print(df); print('--')

df.loc['Aug', 'Math'] = 75
print(df); print('--')

df.loc['Sep', ['Music', 'Sports']] = 76
print(df); print('--')

df.loc['Jul', ['Math', 'Sports']] = 81, 45
print(df); print('--')

print(df.Math); print('--')