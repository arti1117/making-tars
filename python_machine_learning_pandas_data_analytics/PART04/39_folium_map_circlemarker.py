#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:03:24 2020

@author: arti
"""

import pandas as pd
import folium

df = pd.read_excel('./Location_University_in_Seoul.xlsx')

seoul = folium.Map(loaction=[37.55, 126.98], tiles='Stamen Terrain',
                   zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=10,
                        color='red',
                        fill=True,
                        fill_color='yellow',
                        fill_opacity=0.7,
                        popup=name)\
                        .add_to(seoul)

seoul.save('./seoul_university2.html')

