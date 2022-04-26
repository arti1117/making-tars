#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 19:17:45 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

cylinders_size = df.cylinders / df.cylinders.max() * 300

df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5),
        cmap='viridis', c=cylinders_size, s=50, alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')

plt.savefig('./Scatter.png')
plt.savefig('./ScatterTransparent.png', transparent=True)
plt.show()