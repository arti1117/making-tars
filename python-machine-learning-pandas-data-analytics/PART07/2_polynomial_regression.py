#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:15:49 2020

@author: arti
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]

x = ndf[['weight']]
y = ndf['mpg']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, 
                                                    random_state=10)

print('Training data: ', x_train.shape)
print('Validation data: ', x_test.shape)
print('--')

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
x_train_poly = poly.fit_transform(x_train)

print('Origin data: ', x_train.shape)
print('2차항 변환 데이터:', x_train_poly.shape)
print('--')

pr = LinearRegression()
pr.fit(x_train_poly, y_train)

x_test_poly = poly.fit_transform(x_test)
r_square = pr.score(x_test_poly, y_test)

print(r_square)
print('--')

y_hat_test = pr.predict(x_test_poly)

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(x_train, y_train, 'o', label='Train Data')
ax.plot(x_test, y_hat_test, 'r+', label='Predicted Value')
ax.legend(loc='best')

plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()

x_poly = poly.fit_transform(x)
y_hat = pr.predict(x_poly)

plt.figure(figsize=(10, 5))

ax1 = sns.distplot(y, hist=False, label='y')
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)
plt.show()
plt.close()
