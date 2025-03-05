#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:06:58 2020

@author: arti
"""

import pandas as pd
import folium
import json

file_path = './Gyeonggi-do_Population_Data.xlsx'
df = pd.read_excel(file_path, index_col='구분')
df.columns = df.columns.map(str)

geo_path = './Gyeonggi_Provincial_Administrative_Region_Boundary.json'

try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))
    
g_map = folium.Map(location=[37.5502, 126.982],
                   tiles='Stamen Terrain', zoom_start=12)

year = '2007'

folium.Choropleth(geo_data=geo_data,
                  data = df[year],
                  columns = [df.index, df[year]],
                  fill_color = 'YlOrRd', fill_opacity=0.7, line_opacity=0.3,
                  threshold_scale=[10000, 100000, 300000, 500000, 700000],
                  key_on='feature.properties.name',
                  ).add_to(g_map)

g_map.save('./gyeonggi_population_'+year+'.html')