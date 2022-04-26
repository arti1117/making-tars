#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:46:39 2020

@author: arti
"""

import pandas as pd

titanic = pd.read_csv('./titanic.csv')

pd.set_option('display.max_columns', 10)

mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5

df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())
print('--')

isin_filter = titanic['sibsp'].isin([3, 4, 5])
df_isin = titanic[isin_filter]
print(df_isin.head())
