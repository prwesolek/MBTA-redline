import pandas as pd
import sys
import statsmodels.api as sm
import scipy


    #These write some basic stats into an outfile for the various tests. These could probably be combined.
def basicinfowritertime(outfilename,mean1, mean2,std1,std2,year):
    outfilename.write("Summer is defined to be April, May, June, July, August, September, October, and November."+
                      " Winter is defined to be December, January, Feburary, and March.\n\n")
    outfilename.write("The mean on-time performance on summer days for "+year+" is "+
                  str(mean1)+".\n")
    outfilename.write("The standard deviation of the on-time performance on summer days for "+year+" is "+
                      str(std1)+".\n\n")
    outfilename.write("The mean on-time performance on winter days for "+year+" is "+
                  str(mean2)+".\n")
    outfilename.write("The standard deviation of the on-time performance on winter days for "+year+" is "+
                      str(std2)+".\n\n")
    
def basicinfowriterprecip(outfilename,mean1, mean2,std1,std2,name):
    outfilename.write("The mean on-time performance on days with "+name+" is "+
                  str(mean1)+".\n")
    outfilename.write("The standard deviation of the on-time performance on days with "+name+" is "
                  +str(std1)+".\n\n")
    outfilename.write("The mean on-time performance on days withOUT "+name+" is "+
                  str(mean2)+".\n")
    outfilename.write("The standard deviation of the on-time performance on days withOUT "+name+" is "
                  +str(std2)+".\n\n")
    
   
def basicinfowritertemp(outfilename,mean1, mean2,std1,std2,name,tem):
    outfilename.write("The mean on-time performance on days with "+name+" above "+tem+" is "+
                  str(mean1)+".\n")
    outfilename.write("The standard deviation of the on-time performance on days with "+name+" above "+tem+
                      " is "+str(std1)+".\n\n")
    outfilename.write("The mean on-time performance on days with "+name+" below or equal "+tem+" is "+
                  str(mean2)+".\n")
    outfilename.write("The standard deviation of the on-time performance on days with "
                      +name+" below or equal "+tem + " is "+str(std2)+".\n\n")
       
     #This test checks if the on-time performance is affected by the season -  winter or summer.
def time(filename):
    print("running season test...")
    data=pd.read_csv(filename) #read in csv file
    
    #figure out which year we are looking at
    year="" 
    if "2018" in filename:
        year="2018"
    if "2017" in filename:
        year="2017"
        
    #make a string to lable outfiles as peak or offpeak
    tod=""
    if 'offpeak' in filename:
        tod='offpeak'
    else:
        tod='peak'
    
    #get data for winter and data for summer
    dataW=data[((data['date']>=year+'-01-01') & (data['date']<=year+'-03-31')|
              ((data['date']>=year+'-12-01') & (data['date']<=year+'-12-31')))]
        
    dataS=data[~((data['date']>=year+'-01-01') & (data['date']<=year+'-03-31')|
              ((data['date']>=year+'-12-01') & (data['date']<=year+'-12-31')))]
    
    #compute means and standard deviations
    Sstat=dataS['ontime'].describe()
    Smean=Sstat.loc['mean']
    Sstd=Sstat.loc['std']
    
    Wstat=dataW['ontime'].describe()
    Wmean=Wstat.loc['mean']
    Wstd=Wstat.loc['std']
    
    #Run U-test 
    (stat,p)=scipy.stats.mannwhitneyu(dataS['ontime'],dataW['ontime'], alternative='greater')
    
    sign=0 # this variable checks to see if we need to close a file at the end.
    
    #These conditions check if the p-value from the U-test is small. If so, it writes a report to a txt file.
    #If the p-value is large, it prints a failure notice to the command line.
    if p<=.05:
        outfile=open("test-results-"+year+"/"+tod+"season.txt",'w',)
        basicinfowritertime(outfile,Smean,Wmean,Sstd,Wstd,tod)
        outfile.write("With 95% confidence the on-time performance in summer is better than the"+
                      " on-time performance in winter."+
                      " This test is for time-year "+tod+"-"+year+".\n\n")
        print("Season test successful. See output txt file.")
        sign=sign+1
    elif p<=.1:
        outfile=open("test-results-"+year+"/"+tod+"season.txt",'w',)
        basicinfowritertime(outfile,Smean,Wmean,Sstd,Wstd,tod)
        outfile.write("With 90% confidence the on-time performance in summer is better than the"+
                      " on-time performance in winter."+
                      " This test is for time-year "+tod+"-"+year+".\n\n")
        print("Season test successful. See output txt file.")
        sign=sign+1

    else:
        print("Season test fails, because the p-value of",p," is large.")
        
    #If our loop ever opened a file, this final if clause will close it.
    if sign!=0:
        outfile.close()
        
    #This test checks if precipitation or snow affect on-time performance.
def precip(filename):
    print("running precip test...")
    tod=""
    if 'offpeak' in filename:
        tod='offpeak'
    else:
        tod='peak'     
    year="" 
    if "2018" in filename:
        year="2018"
    if "2017" in filename:
        year="2017"
     
    data=pd.read_csv(filename,index_col="date")#read in csv file

           
    sign=0# this variable checks to see if we need to close a file at the end.
    
    #we run two loops. One loop tests snow and the other precipitation.
    for sorp in ["snow","precip"]:
        #cut up dataframe and compute mean and std of on-time performance
        precip=data[(data[sorp]!='0')]
        precipstat=precip['ontime'].describe()
        precipmean=precipstat.loc['mean']
        precipstd=precipstat.loc['std']
        
        noprecip=data[data[sorp]=='0']
        noprecipstat=noprecip['ontime'].describe()
        noprecipmean=noprecipstat.loc['mean']
        noprecipstd=precipstat.loc['std']
        
        #Mann-Whitney U-test for noprecip on-time data greater than precip on-time data
        (stat,p)=scipy.stats.mannwhitneyu(noprecip['ontime'],precip['ontime'], alternative='greater')
        
        #These conditions check if the p-value from the U-test passes. If so, it writes a report to a txt file.
        #If the p-value is too large, it prints a failure notice to the command line.
        if p<=.05:
            outfile=open("test-results-"+year+"/"+tod+"-"+sorp+".txt",'w',)
            basicinfowriterprecip(outfile,precipmean,noprecipmean,precipstd,noprecipstd,sorp)
            outfile.write("With 95% confidence the on-time performance on days withOUT "+sorp+
                          " is better than the on-time performance on days with "+sorp+
                          ". This test is for time-year "+tod+"-"+year+".\n\n")
            print("Test for precipitation type ",sorp," is successful. See output txt file.")
            sign=sign+1
        
        elif p<=.1:
            outfile=open("test-results-"+year+"/"+tod+"-"+sorp+".txt",'w',)
            basicinfowriterprecip(outfile,precipmean,noprecipmean,precipstd,noprecipstd,sorp)
            outfile.write("With 90% confidence the on-time performance on days withOUT "+sorp+
                          " is better than the on-time performance on days with "+sorp+
                          ". This test is for time-year "+tod+"-"+year+".\n\n")
            print("Test for precipitation type ",sorp," is successful. See output txt file.")
            sign=sign+1
        
        else:
            print("Test for precipitation type ",sorp," fails because p value of ",p," is large.")
    
    if sign!=0:  
        outfile.close()
    
    #This test checks if temperature affects on-time performance. The code is similar to that of the precip test.
def temp(filename,temp):
    print("running temp test...")
    t=str(temp)
    temp=float(temp)
    tod="peak"
    if 'offpeak' in filename:
        tod='offpeak'
    year="" 
    if "2018" in filename:
        year="2018"
    if "2017" in filename:
        year="2017"
        
    data=pd.read_csv(filename,index_col="date")
    
    sign=0
    for ht in ['high','low']:   
        aboveF=data[data[ht]>temp]
        aboveFstat=aboveF['ontime'].describe()
        aboveFmean=aboveFstat.loc['mean']
        aboveFstd=aboveFstat.loc['std']
        
        belowF=data[(data[ht]<=temp)]
        belowFstat=belowF['ontime'].describe()
        belowFmean=belowFstat.loc['mean']
        belowFstd=belowFstat.loc['std']
       
        (stat,p)=scipy.stats.mannwhitneyu(aboveF['ontime'],belowF['ontime'], alternative='greater')
        
        if p<=.05:
            outfile=open("test-results-"+year+"/"+tod+"-"+ht+t+".txt",'w',)
            basicinfowritertemp(outfile,aboveFmean,belowFmean,aboveFstd,belowFstd,ht,t)
            outfile.write("With 95% confidence the on-time performance with "+ht+" temps ABOVE "
                          +t+" is better than the on-time performance with "+
                          ht+" temps BELOW "+t+
                          ". This test is for time-year "+tod+"-"+year+".\n\n")
            print("Temp test successful for "+ht+" temp data. See output txt file.")
            sign=sign+1

        elif p<=.1:
            outfile=open("test-results-"+year+"/"+tod+"-"+ht+t+".txt",'w',)
            basicinfowritertemp(outfile,aboveFmean,belowFmean,aboveFstd,belowFstd,ht,t)
            outfile.write("With 90% confidence the on-time performance with "+ht+" temps ABOVE "
                          +t+" is better than the mean on-time performance with "+
                          ht+" temps BELOW "+t+
                          ". This test is for time-year "+tod+"-"+year+".\n\n")
            print("Temp test successful for "+ht+" temp data. See output txt file. ")
            sign=sign+1

        else:
            print("Temp test fails for ",ht," temp data, because the p-value of",p," is large.")
    
    if sign!=0:
        outfile.close()

def main_loop(file):
    print("We will run three tests: Temperature, Season, and Precipitation. ") # some info out to the command line
    tm=input("At which temperature do you want to run the temperature test? ")#ask for temp input
    temp(file,tm)
    time(file)
    precip(file)
    
if __name__ == '__main__':
    main_loop(sys.argv[1])
