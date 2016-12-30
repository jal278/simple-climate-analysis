import pandas

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

import pdb

def load_co2(fname='co2-mm-mlo.csv'):
 data=pandas.read_csv(fname)
 year_decimal=data['Decimal Date']
 co2_decimal=data['Trend']
 data = pandas.DataFrame({'year_decimal':year_decimal,'co2':co2_decimal})
 return data

def load_temp(fname='GLB.Ts.csv'):
 #this data gives one row per year, 12 columns with temperature per month
 data=pandas.read_csv(fname,skiprows=1)

 year_decimal = []
 temp_decimal = []

 #loop through rows of data file
 for idx,row in data.iterrows():
 
  #grab year
  year = row['Year']
 
  #there's a column for each month
  for m_idx,month in enumerate(months):
   #get temperature data for month
   data = row[month]

   try:
    #convert temperature to floating point number
    data = float(data)
    #create floating point year, based on middle of month: 
    #January 2012 = 2012 + 0.5/11
    #February 2012 = 2012 + 1.5/11
    #etc. for easier plotting
    year_decimal.append(year+(m_idx+0.5)/11.0)
    temp_decimal.append(data)
   except:
    #at the end of the current year, i.e. the future, we won't have data
    print "column not available:",year,month
 
 data = pandas.DataFrame(data={'year_decimal':year_decimal,'temp':temp_decimal})
 return data


if __name__=='__main__':
 co2_data = load_co2()
 temp_data = load_temp()

 from pylab import *
 subplot(211)
 plot(co2_data['year_decimal'],co2_data['co2'])
 subplot(212)
 plot(temp_data['year_decimal'],temp_data['temp'])
 show()

