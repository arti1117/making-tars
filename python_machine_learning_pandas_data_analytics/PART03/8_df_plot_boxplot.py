#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:37:01 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv')

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df.plot(kind='box')
df[['mpg', 'cylinders']].plot(kind='box')