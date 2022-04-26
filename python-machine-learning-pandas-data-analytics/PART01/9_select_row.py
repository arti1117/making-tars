#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 05:47:19 2020

@author: arti
"""

import pandas as pd

exam_data = {'Math': [90, 80, 70], 'English': [89, 99, 50],
             'Music': [50, 70, 100], 'Sports': [70, 30, 100]}

df = pd.DataFrame(exam_data, index=['Sep', 'Jul', 'Aug'])


label1 = df.loc['Sep']
position1 = df.iloc[0]

print(label1)
print('----------')
print(position1)

print('----------')
label2 = df.loc[['Jul', 'Aug']]
position2 = df.iloc[[1, 2]]

print(label2)
print('----------')
print(position2)

print('----------')
label3 = df.loc['Jul': 'Aug']
position3 = df.iloc[1: 2]

print(label3)
print('----------')
print(position3)
