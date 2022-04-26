#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:37:29 2020

@author: arti
"""

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[6,5,4], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df); print('--')

ndf = df.sort_values(by='c1', ascending=False)
print(ndf); print('--')
