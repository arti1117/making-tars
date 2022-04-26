#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:36:13 2020

@author: arti
"""

import googlemaps
import panda as pd

my_key = ""

maps = googlemaps.Client(key=my_key)

lat = []
lng = []

places = ["서울시청","국립국악원","해운대해수욕장"]

i = 0
for place in places:
    i = i + 1
    try:
        print(i, place)
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
        
    except:
        lat.append('')
        lng.append('')
        print(i)
        
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print(df)