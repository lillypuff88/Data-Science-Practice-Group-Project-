#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:54:03 2024

@author: crystaldias
"""

import pandas as pd 


bb = pd.read_csv('dsprojus.csv')  
x = []
Daily_deaths = bb.groupby('Last_Update')['Deaths'].sum()
recovered  = bb.groupby('Last_Update')['Recovered'].sum()
confirmed = bb.groupby('Last_Update')['Confirmed'].sum()
x.append(Daily_deaths)
x.append(recovered)
x.append(confirmed)

combined_df = pd.DataFrame()
combined_df = pd.DataFrame(x)
combined_df.to_csv('usonly.csv', index = True)

cc=pd.read_csv('usonly.csv')
transposed = cc.transpose()
transposed.to_csv('usonly.csv')