#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:46:08 2020

@author: arti
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.head())
print('--')
print(titanic.info())