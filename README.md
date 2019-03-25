# MBTA-redline
This project aims to determine what weather factors - e.g. temperature or precipitation - impact the MBTA redline on time performance. 

The extract-red-improved3.py is a python script to be ran from the command line.  The script combines and cleans the raw data from the directory 2018-ontime-performance and the weather data 2018-weather-data.csv and outputs two csv files peak-2018.csv and offpeak-2018.csv. The outputs contain the ontime percent, high temperature, low temperature, precipitation, and snow for each day. The peak-2018.csv file contains the data for the peak hours while the offpeak-2018.csv contains the data for the off-peak hours. Note that weekends and holidays do not have peak hours, so these dates are omitted in peak-2018.csv. 


We now test several hypotheses about our data.\n
(1) Ontime performance for days with high temps above 32 is better than ontime performance for days with high temps below 32.\n
(2) Ontime performance for days with low temps above 32 is better than ontime performance for days with low temps below 32.\n
(3) Ontime performance for days without precipitation is better than ontime performance for days with precipitation.\n
(4) Ontime performance for days without snow is better than ontime performance for days with snow.\n
(5)  Ontime performance for days in summer (april, may, june, july, august, september, october, and november) is better than ontime performance for days in winter (december, january, february, march).\n

We test the hypotheses via the Mann-Whitney U-test, because the data do not appear to be normally distributed. 

