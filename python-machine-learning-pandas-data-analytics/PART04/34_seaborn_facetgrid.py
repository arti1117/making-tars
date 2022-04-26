#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:35:14 2020

@author: arti
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = pd.read_csv('titanic.csv')

sns.set_style('whitegrid')

g = sns.FacetGrid(data=titanic, col='who', row='survived')

g = g.map(plt.hist, 'age')