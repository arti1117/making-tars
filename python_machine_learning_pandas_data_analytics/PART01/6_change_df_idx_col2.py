#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 05:20:12 2020

@author: arti
"""

import pandas as pd

df = pd.DataFrame([[15, 'Boy', 'Apple'], [17, 'Girl', 'Peach']],
                  index=['Jun', 'Jul'],
                  columns=['Age', 'Gender', 'Fruit'])

print(df)

df.rename(columns={'Age':'Ages', 'Gender':'Boy & Girl', 'Fruit':'Nick'}, inplace=True)
df.rename(index={'Jun':'Student1', 'Jul':'Student2'}, inplace=True)

print(df)