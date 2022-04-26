#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:39:29 2020

@author: arti
"""

import folium

sangju_map = folium.Map(location=[36.410799, 128.159039], zoom_start=12)

sangju_map.save('./sangju.html')