# -*- coding: utf-8 -*-
import pandas as pd
import glob
import matplotlib.pyplot as plt
import datetime

path = 'C:/Users/Harsh/OneDrive - University of Kent/DataScience_projecct/jan 21.22.23'
csv_files = glob.glob(path +('/*.csv'))

#iterating through the directoring and reading each csv file to 
#find the selected country and its coresponding data.

'''
data_frame = pd.DataFrame()
#content = []

for filename in csv_files:
    df = pd.read_csv(filename,usecols=['Deaths','Recovered','Confirmed','Country_Region'])
    content = (df[df['Country_Region'] == 'United Kingdom'])
    date = filename.rsplit('.',maxsplit=1)[0]
    date = date.rsplit('\\')[-1]
    date = date.rsplit('-')
    a = date[0]
    b = date[1]
    date[0]=b
    date[1] = a
    date = date[0] +'-'+date[1]+'-'+date[2]#
    content = content.assign(Date = date)
    data_frame = pd.concat([content,data_frame])
   

data_frame.to_csv('uk.csv')


'''













