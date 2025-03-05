#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:37:36 2020

@author: arti
"""

import pandas as pd

df = pd.read_csv('./titanic.csv')

print(df.head())
print('--')

pd.set_option('display.max_columns', 15)
print(df.head())
print('--')

print(df.info())
print('--')

rdf = df.drop(['deck', 'embark_town'], axis = 1)
print(rdf.columns.values)

rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))

most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)
print('--')

print(rdf.describe(include='all'))
print('--')

rdf['embarked'].fillna(most_freq, inplace=True)

ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())

onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head())

x = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male',
         'town_C', 'town_Q', 'town_S']]
y = ndf['survived']

from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
                                                    random_state=10)

print('train data :', x_train.shape)
print('test data :', x_test.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(x_train, y_train)
y_hat = knn.predict(x_test)

print(y_hat[0:10])
print(y_test.values[0:10])

from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)

knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)
