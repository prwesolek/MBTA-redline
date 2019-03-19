#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:31 2019

@author: bhula-wesolekhousehold
"""
import sys
import pandas as pd
import os

#directory=sys.argv[1]

#%%
def redlineisolator(filename):
    data = pd.read_csv(directory+"/"+filename, index_col=6, header=None)
    data.index.rename("date",inplace=True)
    data=data[data[0]=='Red']
    data['ontime']=data[9]/data[10]
    data=data.loc[:,[7,'ontime']]
    return data.groupby(by=7)
#%%
def weathercleaner():
#Import csv file and set index to be 'Day' column
    w_data=pd.read_csv("2018-weather-data.csv", index_col=['Day'])
#Renames columns
    w_data=w_data.rename(columns={'High\n\n(°F)':'high','Low\n\n(°F)':'low',
                                  'Precip.\n\n(inch)':'precip',
                                  'Snow\n\n(inch)':'snow'})
#Properly format index
    w_data.index=pd.to_datetime(w_data.index)
#Eliminate all columns except temperature and precipitation columns.
    w_data=w_data.loc[:,['high','low','precip','snow']]

    return w_data

def main_loop():
    weatherdata=weathercleaner()#Run weather cleaner to get the weather data in the right form.
    files=os.listdir(directory)#Open the directory with the ontime data.
    framesp=[] #list of dataframes for peak times
    framesop=[] # list of dataframes for offpeak times
    for filename in files: #Run throught csv files in directory applying redlineisolator to each
        df_p=redlineisolator(filename).get_group('PEAK')
        df_op=redlineisolator(filename).get_group('OFF_PEAK')
        framesp.append(df_p)
        framesop.append(df_op)
#Put peak and offpeak dataframes together into a peak fram and an off peak frame
    peak_data=pd.concat(framesp)
    offpeak_data=pd.concat(framesop)
#Merge peak_data with weathedata and offpeak_data with weatherdata 
    PDW=pd.merge(peak_data, weatherdata, how='left', left_index=True, right_index=True) 
    oPDW=pd.merge(offpeak_data, weatherdata, how='left', left_index=True, right_index=True) 
#Some final cleaning
    PDW=PDW.sort_values(by='date')
    del PDW[7]
    oPDW=oPDW.sort_values(by='date')
    del oPDW[7]
#Write to csv
    PDW.to_csv("peak-2018.csv", sep=',', encoding='utf-8')
    oPDW.to_csv("offpeak-2018.csv", sep=',', encoding='utf-8')
    
if __name__ == '__main__':
    directory="2018-ontime-performance" #you could write this script to take the directory as an input. 
    main_loop()
 