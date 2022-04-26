#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 05:11:21 2020

@author: arti
"""

import pandas as pd

df = pd.DataFrame([[15, 'Boy', 'Apple'], [17, 'Girl', 'Peach']],
                  index=['Jun', 'Jul'],
                  columns=['Age', 'Gender', 'Fruit'])

print(df)

print(df.index)

print(df.columns)

df.index = ['Student1', 'Student2']
df.columns = ['Ages', 'Boy & Girl', 'Nick Name']

print(df)