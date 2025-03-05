#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 06:11:52 2020

@author: arti
"""

import pandas as pd
import matplotlib.pyplot as plt

# uci_path = "https://archive.ics.uci.edu/ml/machine-learning-databases/\
# 00292/Wholesale%20customers%20data.csv'
df = pd.read_csv('./Wholesale customers data.csv', header=0)

print(df.head())
print(df.info())
print(df.describe())
print('--')

x = df.iloc[:, :]

print(x[:5])
print('--')

from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)

print(x[:5])
print('--')

from sklearn import cluster

kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

kmeans.fit(x)

cluster_label = kmeans.labels_

print(cluster_label)
print('--')

df['Cluster'] = cluster_label
print(df.head())

df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
        colorbar=False, figsize=(10, 10))
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1',
        colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[~mask]


ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
        colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1',
        colorbar=True, figsize=(10, 10))
plt.show()
plt.close()