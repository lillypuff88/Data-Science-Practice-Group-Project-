# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:23:39 2024

@author: lucyp
"""

import glob
import pandas as pd

column_names=['Country_Region', 'Country/Region']
FijiOnly=pd.DataFrame()

for filename in glob.glob('C:/Users/lucyp/Desktop/RealData/*'):
    df = pd.read_csv(filename)
    columns = list(df.columns)
    for name in column_names:
        if name in columns:
            result = df[df[name] == 'Fiji']
            short_filename=filename.rsplit('.', maxsplit=1)[0]
            short_filename=short_filename.rsplit('\\')[-1 ]
            short_filename=short_filename.rsplit('-') 
            a=short_filename[0]
            b=short_filename[1]
            short_filename[0]=b
            short_filename[1]=a
            short_filename=short_filename[0]+'-'+short_filename[1]+'-'+short_filename[2]
            result = result.assign(File=short_filename)
            FijiOnly=pd.concat([result,FijiOnly])
    
            
            
FijiOnly.to_excel('C:/Users/lucyp/Desktop/RealData/FijiOnly.xlsx', index=False)