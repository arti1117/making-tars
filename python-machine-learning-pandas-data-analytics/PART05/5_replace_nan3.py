#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:16:32 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./titanic.csv')

print(df['embark_town'][825:830])
print('--')

df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])