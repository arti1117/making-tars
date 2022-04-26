#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:04:54 2020

@author: arti
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = pd.read_csv('titanic.csv')

sns.set_style('darkgrid')

table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

sns.heatmap(table,
            annot=True, fmt='d',
            cmap='YlGnBu',
            linewidth=.5,
            cbar=False
            )

plt.show()
