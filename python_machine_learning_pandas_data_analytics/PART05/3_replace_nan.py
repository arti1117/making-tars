#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:09:03 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./titanic.csv')

print(df['age'].head(10))

mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))