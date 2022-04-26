#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:43:02 2020

@author: arti
"""

import pandas as pd

student1 = pd.Series({'Korean':100, 'English':80, 'Math':99})
print(student1); print('--')

percentage = student1 / 200

print(percentage); print('--')
print(type(percentage))