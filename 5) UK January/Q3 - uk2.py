# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:31:04 2024

@author: Harsh
"""
# summing the data  for each category 
'''
import pandas as pd
combined_df = pd.DataFrame()
aa = pd.read_csv('uk.csv')
ct = []
Daily_deaths = aa.groupby('Date')['Deaths'].sum()
recovered  = aa.groupby('Date')['Recovered'].sum()
confirmed = aa.groupby('Date')['Confirmed'].sum()
ct.append(Daily_deaths)
ct.append(recovered)
ct.append(confirmed)



combined_df = pd.DataFrame(ct)
combined_df.to_csv('uk2.csv',mode='a', index = True)
'''
#transposing the data
'''
data = pd.read_csv('uk2.csv')
transposed = data.transpose(header = False)
transposed.to_csv('uk2.csv')
'''