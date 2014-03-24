#
# Load modules
#

import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import mpl_toolkits.basemap as bm
# Scipy's io module needed to load MATLAB data
from scipy import io
# Load GSW module for TEOS-10 functions (oceanography)
import gsw

#
# T-S diagram
#

# Load data
data = sp.io.loadmat('~/erics_python_plotting/data/temp_depth.mat')
depth = data['depth']
T_CTRL = data['T_CTRL']
T_A1B = data['T_A1B']
S_CTRL = data['S_CTRL']
S_A1B = data['S_A1B']

# Location
lon = 160
lat = -40

# Convert depth to pressure
p = gsw.p_from_z(-depth, lat)

# Convert practical salinity to absolute salinity
SA_CTRL = gsw.SA_from_SP(S_CTRL, p, lon, lat)
SA_A1B = gsw.SA_from_SP(S_A1B, p, lon, lat)

# Convert in-situ temperature to conservative temperature
TC_CTRL = gsw.CT_from_t(SA_CTRL, T_CTRL, p)
TC_A1B = gsw.CT_from_t(SA_A1B, T_A1B, p)

# Calculate density on a T-S grid
T_grid, S_grid = np.meshgrid(np.arange(0,35,0.05), np.arange(33,37,0.001))
rho = gsw.rho(S_grid, T_grid, 0) # SHOULD calc pot. dens. NOT in-situ density assuming no depth

# Plot
plt.figure()

CS = plt.contour(S_grid, T_grid, rho, levels=np.arange(1018,1032,1), colors='k')
plt.plot(SA_CTRL, TC_CTRL, 'k-', marker='o', markeredgecolor='k', linewidth=2)
plt.plot(SA_A1B, TC_A1B, 'r-', marker='o', markeredgecolor='r', linewidth=2)

plt.xlim(34.4,36.0)
plt.ylim(0,22)
plt.grid()
plt.clabel(CS, inline=1, fontsize=10, manual=True) # ESC to end selection

plt.xlabel('Absolute salinity [g/kg]')
plt.ylabel(r'Conservative Temperature [$^\circ$C]')

