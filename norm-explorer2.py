
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
import matplotlib.mlab as mlab


def check_norm_temp_graphical(year,temp): 
    for tod in ['peak','offpeak']:
        data=pd.read_csv("clean-files-"+str(year)+"/"+tod+"-"+str(year)+".csv",index_col="date") #read in data
        for hl in ['high','low']:
            aboveF=data[data[hl]>temp] #above 32 data frame
            belowF=data[data[hl]<=temp] #below 32 data frame
            aboveF=aboveF['ontime'] #reduce to ontime data
            belowF=belowF['ontime'] #reduce to ontime data
            for aob in ['above','below']:
                
                if aob=='above':#finds out which data frame to look at
                    X=aboveF 
                if aob=='below':
                    X=belowF
                X=aboveF 
                mu, sigma = norm.fit(X) #get mean and std from belowF data
                fig1=plt.figure()
                n, bins, patches = plt.hist(X,  bins=50,density=True, alpha=0.9) #make a histogram from X
                xmin, xmax = plt.xlim() #determine the upper and lower limits of the histogram
                x = np.linspace(xmin, xmax, 50) #an array with 50 terms equally spaced from xmin to xmax
                p = norm.pdf(x, mu, sigma)
                plt.plot(x, p, linewidth=2)
                plt.title('Days with '+hl+' '+aob+' '+str(temp))
                plt.ylabel('Frequency')
                plt.xlabel('On-time percent')
                fig1.savefig("graphs/"+str(year)+'/'+tod+'-'+str(year)+'-'+hl+'-'+aob+'-'+str(temp)+".pdf")

def check_norm_analytic(year,temp):
    normdata=[]
    for tod in ['peak','offpeak']:
        data=pd.read_csv("clean-files-"+str(year)+"/"+tod+"-"+str(year)+".csv",index_col="date") #read in data
        for hl in ['high','low']:
            aboveF=data[data[hl]>temp] #above 32 data frame
            belowF=data[data[hl]<=temp] #below 32 data frame
            aboveF=aboveF['ontime'] #reduce to ontime data
            belowF=belowF['ontime'] #reduce to ontime data
            for aob in ['above','below']:
                
                if aob=='above':#finds out which data frame to look at
                    X=aboveF 
                if aob=='below':
                    X=belowF
                X=aboveF 
                
                (s,p)=scipy.stats.normaltest(X) #run normality test. The null hypothesis is "the data is normally distributed."
                
                if p>.05:
                    normdata.append((tod,str(year),hl,aob,str(temp)))
    
    if normdata==[]:
        print("None of the data sets for ",year," are normally distributed.")
    else:
        print("The following data sets for ",year," may be normally distributed: ",normdata)

def main_loop():
    year=input("For which year (2017 or 2018) do you want to run the temperature normality explorer? ") #ask for year input
    tm=input("At which temperature do you want to run the temperature normality explorer? ")#ask for temp input
    temp=float(tm)
    check_norm_temp_graphical(year,temp)
    print("Output graphs can be found in the ",year," directory in the graphs directory.")
    check_norm_analytic(year,temp)
    
    
if __name__ == '__main__':
    main_loop()
