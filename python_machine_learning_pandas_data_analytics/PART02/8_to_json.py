#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:57:19 2020

@author: arti
"""

import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ['A', 'A+', 'B'],
        'basic': ['C', 'B', 'B+'],
        'c++': ['B+', 'C', 'C+']}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)

print(df)

df.to_json('./8_to_json.json')