#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:52:43 2020

@author: arti
"""

import folium

chengdu1 = folium.Map(location=[30.657000, 104.066002], tiles='Stamen Terrain',
                     zoom_start=12)
chengdu2 = folium.Map(location=[30.657000, 104.066002], tiles='Stamen Toner',
                     zoom_start=15)

chengdu1.save('./chengdu1.html')
chengdu2.save('./chengdu2.html')