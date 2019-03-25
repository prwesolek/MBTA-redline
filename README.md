# MBTA-redline
This project aims to determine what weather factors - e.g. temperature or precipitation - impact the MBTA redline ontime performance. 

The extract-red-improved3.py is a python script to be ran from the command line.  The script combines and cleans the raw data from the directory year-ontime-performance and the weather data year-weather-data.csv and outputs two csv files peak-year.csv and offpeak-year.csv. The outputs contain the ontime percent, high temperature, low temperature, precipitation, and snow for each day. The peak-year.csv file contains the data for the peak hours while the offpeak-year.csv contains the data for the off-peak hours. Note that weekends and holidays do not have peak hours, so these dates are omitted in peak-year.csv. 



We now test several hypotheses about our data.

(1) Ontime performance for days with high temps above 32 is better than ontime performance for days with high temps below 32.

(2) Ontime performance for days with low temps above 32 is better than ontime performance for days with low temps below 32.

(3) Ontime performance for days without precipitation is better than ontime performance for days with precipitation.

(4) Ontime performance for days without snow is better than ontime performance for days with snow.

(5)  Ontime performance for days in summer (april, may, june, july, august, september, october, and november) is better than ontime performance for days in winter (december, january, february, march).

We will test the hypotheses for four data sets: 2018 peak hours ontime performance, 2018 offpeak hours ontime performance, 2017 peak hours ontime performance, and 2017 offpeak hours ontime performance. The python script testerU.py tests these hypotheses via the Mann-Whitney U-test. We use the U-test because the data do not appear to be normally distributed. The script is to be ran from the command line and takes one input; the input should be one of the csv files  offpeak-year.csv and peak-year.csv. If the U-test is successful, a report is written into a txt file. Otherwise a failure notice is printed to the command line. 


Test results:

(1) In both 2017 and 2018 on both peak and offpeak hours, ontime performance on days with high temps above 32 is better than ontime performance for days with high temps below 32 with 95% confidence.

(2) In 2017 on both peak and offpeak hours,  ontime performance on days with low temps above 32 is better than ontime performance for days with low temps below 32 with 95% confidence. The test fails for 2018 offpeak and 2018 peak data, so we cannot reject or conclude the hypothesis for these cases.

(3) The test here failed for all data sets. We cannot reject or conclude the hypothesis. 

(4) In 2017 on offpeak hours, ontime performance on days without snow is better than the on-time performance on days with snow. The test fails for 2017 peak, 2018 offpeak, and 2018 peak data, so we cannot reject or conclude the hypothesis for these cases.

(5) The test here failed for all data sets. We cannot reject or conclude the hypothesis.


Conclusions: The results of our tests for hypothesis (1) are good, and we are justifyed in concluding that hypothesis (1) indeed holds. Given the mixed or failure results for hypotheses (2),(3), (4), and (5), I feel more data or better analysis is needed to accept or reject any of these hypotheses.

