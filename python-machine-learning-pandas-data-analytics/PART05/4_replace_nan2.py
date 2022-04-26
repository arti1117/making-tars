#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:11:16 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./titanic.csv')

print(df['embark_town'][825:830])
print('--')

most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)
print('--')

df['embark_town'].fillna(most_freq, inplace=True)
print(df['embark_town'][825:830])
