#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:49:17 2020

@author: arti
"""

import pandas as pd

tup_data = ('JY', '2020-08-04', 'Man', False)
sr = pd.Series(tup_data, index=['Name', 'Date', 'Gender', '?'])

print(sr)

print(sr[0])
print(sr['Name'])
# print(sr['name'])

print(sr[[1, 2]])
print('\n')
print(sr[['Name', 'Gender']])

print('--------------')

print(sr[0:2])
print('\n')
print(sr['Name':'Gender'])