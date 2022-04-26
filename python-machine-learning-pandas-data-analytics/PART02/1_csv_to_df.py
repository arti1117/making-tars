# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

file_path='./read_csv_data.csv'

df1 = pd.read_csv(file_path)
print(df1)

df2 = pd.read_csv(file_path, header=0)
print(df2)

df3 = pd.read_csv(file_path, index_col=None)
print(df3)

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)