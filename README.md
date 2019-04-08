<h2> MBTA-redline</h2>

<h3> Overview </h3>
<p>
This project aims to determine what weather factors - e.g. temperature or precipitation - impact the MBTA redline ontime performance. We use the ontime date from 2017 and 2018. All scripts are designed to be ran on Python3. Click here [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/prwesolek/MBTA-redline/master) to run the jupyter notebooks.</p>

<h3> Cleaning script details</h3>
<p>
The python script extract-clean2.py is to be ran from the command line and when ran will ask for the year, either 2017 or 2018.  The script combines and cleans the raw data from the directory year-ontime-performance and the weather data year-weather-data.csv from the directory weatherdata and outputs two csv files peak-year.csv and offpeak-year.csv into the directory clean-files-year. The outputs contain the ontime percent, high temperature, low temperature, precipitation, and snow for each day for peak hours and offpeak hours, respectively. Note that weekends and holidays do not have peak hours, so these dates are omitted in peak-year.csv. Note also that 2017 data is missing the data for the month of december. </p>


<h3>Analysis script details</h3>
<p>The python script testerU2.py tests several hypotheses via the Mann-Whitney U-test; we use the U-test because the data do not appear to be normally distributed as discussed in the normality explorer section. The script is to be ran from the command line. The script will ask for the year (2017 or 2018), the time of day (peak or off peak), and a temperature as inputs. If the U-test is successful, a report is written into a txt file in the directory test-results-year. If the U-test is unsuccessful a failure notice is printed to the command line. 
</p>

<h3> Hypotheses tested </h3>
<p>
<ol>
<li>Ontime performance for days with high temps above 32 is better than ontime performance for days with high temps below 32.</li>

<li>Ontime performance for days with low temps above 32 is better than ontime performance for days with low temps below 32.</li>

<li> Ontime performance for days without precipitation is better than ontime performance for days with precipitation.</li>

<li> Ontime performance for days without snow is better than ontime performance for days with snow.</li>

<li> Ontime performance for days in summer (april, may, june, july, august, september, october, and november) is better than ontime performance for days in winter (december, january, february, march).</li>
</ol>
</p>

<h3> Normality explorer</h3>
<p> The script norm-explorer2.py checks if the temperature data sets are normally distributed. This program is to be ran from the command line. When ran it will ask for the year and temperature at which you would like to test normality. It applies the D'agostino and Pearson normality test to several data sets to check for normality. These data sets have the following form: the ontime performance data for peak/offpeak times on days with high/low temperatures above/below input temperature. The results are printed to the command line. Graphs are also generated which attempt to fit normal curves to the data; these graphs are written to the graphs directory. </p>

<h3>Results</h3>
<p>
<ol>
<li> In both 2017 and 2018 on both peak and offpeak hours, ontime performance on days with high temps above 32 is better than ontime performance for days with high temps below 32 with 95% confidence.</li>

<li> In 2017 on both peak and offpeak hours,  
  ontime performance on days with low temps above 32 is better than ontime performance for days with low temps below 32 with 95% confidence.</li>

<li> The test here failed for all data sets. We cannot reject or conclude the hypothesis. </li> 

<li> In 2017 on offpeak hours, ontime performance on days without snow is better than the on-time performance on days with snow. The test fails for 2017 peak, 2018 offpeak, and 2018 peak data.</li>

<li> The test here failed for all data sets. We cannot reject or conclude the hypothesis.</li>

</ol>
</p>

<h3>Conclusions</h3>
<p> The result of our test for hypothesis (1) is good, and we are justified in concluding that hypothesis (1) indeed holds. Given the mixed or failure results for hypotheses (2),(3), (4), and (5), I feel more data or better analysis is needed to accept or reject any of these hypotheses. 
 </p>
 
<h3>Further analysis</h3>
<p> 
  <ul>
    <li>The data from 2017 and 2018 should be combined and the tests run on the combined data set. This may give us more power and avoid test failures. </li>
    <li> New hypotheses should be formulated to test if weather has a larger affect on offpeak ontime performance or peak ontime performance.</li>
  </ul>
  </p>

