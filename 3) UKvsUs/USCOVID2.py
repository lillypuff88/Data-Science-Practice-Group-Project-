#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:50:56 2024

@author: crystaldias
"""

import pandas as pd
import matplotlib.pyplot as plt
import glob

path = '/Users/crystaldias/Downloads/covidcases.csv'
all_files = glob.glob(path + "/*.csv")

data_frames = []
for filename in all_files:
    print(f'Loading {filename}')
    new_df = pd.read_csv(filename, usecols=['Deaths', 'Confirmed', 'Recovered', 'Country_Region', 'Province_State', 'Last_Update'])
    data_frames.append(new_df)
    

df = pd.concat(data_frames)

a = df[df['Country_Region'] == 'US']



data_frame = pd.concat([a])

data_frame.to_csv('dsprojus.csv')