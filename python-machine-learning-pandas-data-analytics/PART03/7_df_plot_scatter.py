#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:27:17 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv')

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df.plot(x='weight', y='mpg', kind='scatter')
