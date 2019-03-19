# MBTA-redline
This project aims to determine what weather factors - e.g. temperature or precipitation - impact the MBTA redline on time performance. 

The extract-red-improved3.py is a python script to be ran from the command line.  The script combines and cleans the raw data from the directory 2018-ontime-performance and the weather data 2018-weather-data.csv and outputs two csv files peak-2018.csv and offpeak-2018.csv. The outputs contain the ontime percent, high temperature, low temperature, precipitation, and snow for each day. The peak-2018.csv file contains the data for the peak hours while the offpeak-2018.csv contains the data for the off-peak hours. Note that weekends and holidays do not have peak hours, so these dates are omitted in peak-2018.csv. 


