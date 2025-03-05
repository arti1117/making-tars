#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:24:35 2020

@author: arti
"""

import pandas as pd

df = pd.read_excel('./Amount_of_electricity_generated _by_S.Korea_N.Korea.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

tdf_ns = df_ns.T
print(tdf_ns.head())
tdf_ns.plot(kind='bar')