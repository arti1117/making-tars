#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:35:21 2020

@author: arti
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]

print(df.tail())

addition = df + 10
print(addition.tail())

subtraction = addition - df
print(subtraction.tail())