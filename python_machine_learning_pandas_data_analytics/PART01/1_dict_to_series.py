#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:52:58 2020

@author: arti
"""

import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}

sr = pd.Series(dict_data)

print(type(sr))
print('\n')

print('dict_data:' + str(dict_data))
print('\n')

print('sr:')
print(sr)