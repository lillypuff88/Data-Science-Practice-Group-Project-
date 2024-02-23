# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:33:31 2024

@author: Harsh
"""
import pandas as pd

# collecting data from december 2020 to calculate the daily values in jan 2021
'''
ukonly = pd.DataFrame()
column_names = ['Deaths','Recovered','Confirmed','Country_Region']
df=pd.read_csv('12-31-2020.csv')
columns = list(df.columns)
for name in columns:
    if name in column_names:
        results = df[df[name]=='United Kingdom']
        ukonly = pd.concat([results,ukonly])

ukonly.to_csv('12-31-2020.csv')
'''

#summing the data from each catergory and storing it 
'''
bb = pd.read_csv('12-31-2020.csv')   
x = []
Daily_deaths = bb['Deaths'].sum()
recovered  = bb['Recovered'].sum()
confirmed = bb['Confirmed'].sum()      
x.append(Daily_deaths)
x.append(recovered)
x.append(confirmed)
combined_df = pd.DataFrame()
combined_df = pd.DataFrame(x)
combined_df.to_csv('12-31-2020.csv', index = True)
 '''  


