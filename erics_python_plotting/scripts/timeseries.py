#
# Load modules
#

import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import mpl_toolkits.basemap as bm

#
# Temperature time series
#

# Load data
data = np.load('../data/temp_ts.npz')
time = data['time']
lon = data['lon']
lat = data['lat']
T_CTRL = data['T_CTRL']
T_A1B = data['T_A1B']

# Plot time series
#plt.figure() # One time series
plt.figure(figsize=(14,6)) # One time series
plt.plot(time, T_CTRL[:,1], 'k-')
plt.plot(time, T_A1B[:,1], 'r-')
plt.ylabel(r'Temperature [$^\circ$C]')
plt.xlabel('time [years]')
plt.grid()
plt.savefig('temp_ts_single.png')

plt.figure() # Four time series, as a 4x1 subplot matrix
for i in range(len(lon)):
    plt.subplot(4,1,i+1)
    plt.plot(time, T_CTRL[:,i], 'k-')
    plt.plot(time, T_A1B[:,i], 'r-')
    plt.ylabel(r'Temperature [$^\circ$C]')
    plt.title(str(np.round(lon[i]).astype(int))+r'$^\circ$E '+str(np.round(-lat[i]).astype(int))+r'$^\circ$S')
    plt.grid()
    if i<len(lon)-1:
        locs, labels = plt.xticks()
        plt.xticks(locs, [])
    else:
        plt.xlabel('time [years]')

plt.savefig('temp_ts_four.png')

#
# Histogram and probability density function
#

# Simple histogram
plt.figure()
plt.hist(T_CTRL[:,1], 30)
plt.ylabel('Count')
plt.xlabel(r'Temperature [$^\circ$C]')

plt.savefig('histogram.png')

# Calculate pdf using a kernel density function
from scipy import stats # need this extra module
T = np.arange(10,25,0.01) # Define range over which to calculate pdf
kernel = sp.stats.gaussian_kde(T_CTRL[:,1])
T_CTRL_pdf = kernel.evaluate(T)

plt.figure()
plt.plot(T, T_CTRL_pdf, 'k-')
plt.ylabel('Probability')
plt.xlabel(r'Temperature [$^\circ$C]')

# Add the other curve (for T_A1B)
kernel = sp.stats.gaussian_kde(T_A1B[:,1])
T_A1B_pdf = kernel.evaluate(T)
plt.plot(T, T_A1B_pdf, 'r-')

# Add a legend
plt.legend(('CTRL run', 'A1B run'))

plt.savefig('pdf_1.png')

# Calculate pdf using a kernel density function
plt.figure()
sec = np.arange(np.percentile(T_CTRL[:,1], 2.5), np.percentile(T_CTRL[:,1], 97.5), 0.01)
kernel = sp.stats.gaussian_kde(T_CTRL[:,1])
fill = kernel.evaluate(sec)
plt.fill_between(sec, fill, color=[0.65,0.65,0.65])
plt.plot(T, T_CTRL_pdf, 'k-')
plt.ylim(0,T_CTRL_pdf.max()*1.1)
plt.ylabel('Probability')
plt.xlabel(r'Temperature [$^\circ$C]')

plt.savefig('pdf_2.png')
