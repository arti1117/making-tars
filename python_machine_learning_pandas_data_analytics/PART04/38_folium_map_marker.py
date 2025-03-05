#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:35:35 2020

@author: arti
"""

import pandas as pd
import folium

df = pd.read_excel('./Location_University_in_Seoul.xlsx')

seoul = folium.Map(loaction=[37.55, 126.98], tiles='Stamen Terrain',
                   zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul)

seoul.save('./seoul_university.html')