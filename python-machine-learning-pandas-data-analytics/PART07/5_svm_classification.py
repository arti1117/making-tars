#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:14:33 2020

@author: arti
"""

import pandas as pd
import seaborn as sns

df = pd.read_csv('./titanic.csv')

pd.set_option('display.max_columns', 15)

rdf = df.drop(['deck', 'embark_town'], axis=1)

rdf = rdf.dropna(subset=['age'], how='any', axis=0)

most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
rdf['embarked'].fillna(most_freq, inplace=True)

ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]

onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)

x = ndf [['pclass', 'age', 'sibsp', 'parch', 'female', 'male',
          'town_C', 'town_Q', 'town_S']]
y = ndf['survived']

from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
                                                    random_state=10)
print('train data :', x_train.shape)
print('test data :', x_test.shape)

from sklearn import svm

svm_model = svm.SVC(kernel='rbf')

svm_model.fit(x_train, y_train)
y_hat = svm_model.predict(x_test)

print(y_hat[0:10])
print(y_test.values[0:10])

from sklearn import metrics

svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)