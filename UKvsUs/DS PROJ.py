#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:29:02 2024

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
    new_df = pd.read_csv(filename, usecols=['Deaths', 'Confirmed', 'Recovered', 'Country_Region', 'Province_State'])
    data_frames.append(new_df)

df = pd.concat(data_frames)

a = df[df['Province_State'] == 'Wales']
b = df[df['Province_State'] == 'England']
c = df[df['Province_State'] == 'Scotland']
d = df[df['Province_State'] == 'Northern Ireland']

data_frame = pd.concat([a, b, c, d])

