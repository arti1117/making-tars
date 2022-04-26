#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 06:35:11 2020

@author: arti
"""

import pandas as pd
import folium as fm

file_path = './2016_middle_shcool_graduates_report.xlsx'

df = pd.read_excel(file_path, header=0)

pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

# print(df.columns.values)
# print(df.head())
# print(df.info()) 
# print(df.describe())
# print('--')

mschool_map = fm.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                     zoom_start=12)

for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    fm.CircleMarker([lat, lng],
                      radius=5,
                      color='brown',
                      fill=True,
                      fill_color='coral',
                      fill_opacity=0.7,
                      popup=name).add_to(mschool_map)

mschool_map.save('./Seoul_Middle_School_locations.html')

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

onehot_location = label_encoder.fit_transform(df['지역'])
onehot_code = label_encoder.fit_transform(df['코드'])
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_location
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day

from sklearn import cluster

columns_list = [9, 10, 13]
x = df.iloc[:, columns_list]
x = preprocessing.StandardScaler().fit(x).transform(x)

dbm = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm.fit(x)

cluster_label = dbm.labels_
df['Cluster'] = cluster_label
# print(df.head())
# print('--')

grouped_cols = [0, 1, 3] + columns_list
grouped = df.groupby('Cluster')

#for key, group in grouped:
#    print('* key :', key)
#    print('* number :', len(group))
#    print(group.iloc[:, grouped_cols].head())
#    print('\n')
    
colors = {-1:'gray', 0:'coral', 1:'blue', 2:'green', 3:'red', 4:'purple', 5:'orange',
          6:'brwon', 7:'brick', 8:'yellow', 9:'magenta', 10:'cyan', 11:'purple'}

cluster_map = fm.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                     zoom_start=10)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):
    fm.CircleMarker([lat, lng],
                    radius=5,
                    color=colors[clus],
                    fill=True,
                    fill_color=colors[clus],
                    fill_opacity=0.7,
                    popup=name).add_to(cluster_map)
    
cluster_map.save('./Seoul_Middle_School_Cluster.html')

columns_list2 = [9, 10, 13, 22]
x2 = df.iloc[:, columns_list2]
x2 = preprocessing.StandardScaler().fit(x2).transform(x2)
dbm2 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm2.fit(x2)

df['Cluster2'] = dbm2.labels_

grouped2_cols = [0, 1, 3] + columns_list2
grouped2 = df.groupby('Cluster2')

cluster2_map = fm.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                      zoom_start=11)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):
    fm.CircleMarker([lat, lng],
                    radius=5,
                    color=colors[clus],
                    fill=True,
                    fill_color=colors[clus],
                    fill_opacity=0.7,
                    popup=name).add_to(cluster2_map)

cluster2_map.save('./Seoul_Middle_School_Cluster2.html')

columns_list3 = [9, 10]
x3 = df.iloc[:, columns_list3]
x3 = preprocessing.StandardScaler().fit(x3).transform(x3)
dbm3 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm3.fit(x3)

df['Cluster3'] = dbm3.labels_

grouped3_cols = [0, 1, 3] + columns_list2
grouped3 = df.groupby('Cluster2')

cluster3_map = fm.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                      zoom_start=11)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster3):
    fm.CircleMarker([lat, lng],
                    radius=5,
                    color=colors[clus],
                    fill=True,
                    fill_color=colors[clus],
                    fill_opacity=0.7,
                    popup=name).add_to(cluster3_map)

cluster3_map.save('./Seoul_Middle_School_Cluster3.html')