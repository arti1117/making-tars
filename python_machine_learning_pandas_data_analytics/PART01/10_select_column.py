#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 05:54:42 2020

@author: arti
"""

import pandas as pd

exam_data = {'Name': ['Sep', 'Jul', 'Aug'],
             'Math': [90, 80, 70],
             'English': [89, 99, 50],
             'Music': [50, 70, 100],
             'Sports': [70, 30, 100]}

df = pd.DataFrame(exam_data)

print(df)
print('----------')

math1 = df['Math']
print(math1)
print(type(math1))
print('----------')

english1 = df.English
print(english1)
print(type(english1))
print('----------')

music_and_sports = df[['Music', 'Sports']]
print(music_and_sports)
print(type(music_and_sports))
print('----------')

math2 = df[['Math']]
print(math2)
print(type(math2))
print('----------')
