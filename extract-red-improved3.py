import pandas as pd
import os
import sys


def redlineisolator(filename,directory):
    data = pd.read_csv(directory+"/"+filename, index_col=6, header=None) #import csv file. Column 6 is the date column.
    data.index.rename("date",inplace=True)#rename index as date
    data=data[data[0]=='Red'] #isolate all rows pertaining to redline
    data['ontime']=data[9]/data[10] #make a new column which gives ontime percentage
    data=data.loc[:,[7,'ontime']] #throw away all columns except the column for the peak/off peak designation and ontime percent.
    return data.groupby(by=7) #group data into peak and off peak frames

def weathercleaner(year):
    w_data=pd.read_csv(year+"-weather-data.csv", index_col=['Day']) #import correct weather data csv file and set index to be 'Day' column
    w_data=w_data.rename(columns={'High\n\n(°F)':'high','Low\n\n(°F)':'low',
                                  'Precip.\n\n(inch)':'precip',
                                  'Snow\n\n(inch)':'snow'})#renames columns
    w_data.index=pd.to_datetime(w_data.index)#properly format index
    w_data=w_data.loc[:,['high','low','precip','snow']]#eliminate all columns except temperature and precipitation columns.
    return w_data

def main_loop(directory):
    year=directory.strip("-ontime-performance") #get the year from the directory name
    weatherdata=weathercleaner(year)#Run weather cleaner to get the weather data in the right form.
    files=os.listdir(directory)#Open the directory with the ontime data.
    framesp=[] #list of dataframes for peak times
    framesop=[] # list of dataframes for offpeak times
    for filename in files: #Run throught csv files in directory applying redlineisolator to each
        df_p=redlineisolator(filename,directory).get_group('PEAK')
        df_op=redlineisolator(filename,directory).get_group('OFF_PEAK')
        framesp.append(df_p)
        framesop.append(df_op)
#Put peak and offpeak dataframes together into a peak frame and an off peak frame
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
    PDW.to_csv("peak-"+year+".csv", sep=',', encoding='utf-8')
    oPDW.to_csv("offpeak-"+year+".csv", sep=',', encoding='utf-8')
    
if __name__ == '__main__': 
    direct=sys.argv[1]
    main_loop(direct)
 
