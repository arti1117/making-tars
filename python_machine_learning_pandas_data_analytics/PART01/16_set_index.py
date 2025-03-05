#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:05:43 2020

@author: arti
"""

import pandas as pd

exam_data = {'Name': ['Sep', 'Jul', 'Aug'],
             'Math': [90, 80, 70],
             'English': [89, 99, 50],
             'Music': [50, 70, 100],
             'Sports': [70, 30, 100]}

df = pd.DataFrame(exam_data)

print(df); print('--')

dft = df.set_index(['Name'])
print(dft); print('--')

dftt = dft.set_index('Music')
print(dftt); print('--')

ndf = dft.set_index(['Math', 'Music'])
print(ndf); print('--')


