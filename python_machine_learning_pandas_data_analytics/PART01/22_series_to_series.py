#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:49:59 2020

@author: arti
"""

import pandas as pd

student1 = pd.Series({'Korean':100, 'English':80, 'Math':99})
student2 = pd.Series({'Math':100, 'Korean':80, 'English':75})
print(student1); print('--')
print(student2); print('--')

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2

print(type(division)); print('--')

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['Addition', 'Subtraction', 'Multiplication', 'Division'])

print(result)
