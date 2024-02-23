#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:35:18 2024

@author: crystaldias
"""
import pandas as pd 


bb = pd.read_csv('dsprojdates.csv')  
x = []
Daily_deaths = bb.groupby('dates')['Deaths'].sum()
recovered  = bb.groupby('dates')['Recovered'].sum()
confirmed = bb.groupby('dates')['Confirmed'].sum()
x.append(Daily_deaths)
x.append(recovered)
x.append(confirmed)

combined_df = pd.DataFrame()
combined_df = pd.DataFrame(x)
combined_df.to_csv('ukonly.csv', index = True)

cc=pd.read_csv('ukonly.csv')
transposed = cc.transpose()
transposed.to_csv('ukonly.csv')
