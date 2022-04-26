#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:26:36 2020

@author: arti
"""

import pandas as pd

pr_m = pd.period_range(start='2019-01-01',
                       end=None,
                       periods=3,
                       freq='M')
print(pr_m)

pr_2h = pd.period_range(start='2020-01-01',
                        end='2020-02-01',
                        periods=None,
                        freq='2H')
print(pr_2h)