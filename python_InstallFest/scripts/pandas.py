# Pandas example

#
# Load modules
#
import pandas as pd
import matplotlib.pyplot as plt

#
# Load Data
#
data = pd.read_csv('/Users/Rob_MacPro/Documents/4._Archive/dataSciGroup/githubRepos/DataScienceHobart/python_InstallFest/data/pigmentData.csv')
#
# Print data
#
print data
#
# look at a variable, you can call a column by its name using either square brackets ['name'] or by using .name
#
print data.TimeUTC
print data['TimeUTC']
#
# simple stats can be done in a human readable way, type the following to do sum or std or max or min etc
#
data.Chla.sum()
data.Chla.std()
data.Chla.min()
data.Chla.max()
#
data.Chl_c1.sum()
data.Chl_c1.std()
data.Chl_c1.min()
data.Chl_c1.max()
#
# are there any missing data
#
pd.isnull(data)
#
# simple plots - 1st is a cumulative sum of the chla data. 2nd is a simple subplot of some pigments in our file
#
# 1st
data.Chla.cumsum().plot()
#
# 2nd
fig = plt.figure() # creates an empty window
ax1 = fig.add_subplot(2,2,1) #create empty plots inside the figure window
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(data.Chla,'k--') #plot to the first axis
ax2.hist(data.Chla,bins=8,color='k') #plot to the second axis
ax3.plot(data.Depth,'k--') #plot to the third axis
ax4.hist(data.Depth,bins=10,color='k') #plot to the foth axis

ax1.set_title('Chlorophyll-a line graph') #set some titles.
ax2.set_title('Chlorophyll-a hist')
ax3.set_title('Depth line graph')
ax4.set_title('Depth hist')

ax4.set_xlabel('stuff') #set some axis labels.
#
# save data out as a csv with headers
#
data.to_csv('pandasDataOuput.csv')

