#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 06:25:56 2020

@author: arti
"""

import pandas as pd

file_path = './read_json_data.json'

df = pd.read_json(file_path)

print(df)

print(df.index)