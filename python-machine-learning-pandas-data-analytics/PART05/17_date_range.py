#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:19:14 2020

@author: arti
"""

import pandas as pd

ts_ms = pd.date_range(start='2019-01-01',
                      end=None,
                      periods=6,
                      freq='MS',
                      tz='Asia/Seoul')

print(ts_ms)

ts_3m = pd.date_range('2020-01-01', periods=6,
                      freq='3M', tz='Asia/Seoul')
print(ts_3m)