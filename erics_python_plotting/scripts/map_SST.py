#
# Load modules
#

import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import mpl_toolkits.basemap as bm
# Scipy's io module needed to load MATLAB data
from scipy import io

#
# Mean Temperature
#

# Load data
data = sp.io.loadmat('~/erics_python_plotting/data/OFAM_model_mean.mat')
lon = data['lon']
lat = data['lat']
T_CTRL = data['T_CTRL']
T_A1B = data['T_A1B']
U_CTRL = data['U_CTRL']
V_CTRL = data['V_CTRL']
llon, llat = np.meshgrid(lon, lat)

# Map T_CTRL
plt.figure()
proj = bm.Basemap(projection='merc', llcrnrlat=-50, llcrnrlon=145, urcrnrlat=-20, urcrnrlon=180, resolution='i')
proj.drawcoastlines()
proj.drawparallels([-50,-45,-40,-35,-30,-25,-20], labels=[True,False,False,False])
proj.drawmeridians(range(145,180+1,5), labels=[False,False,False,True])
lonproj, latproj = proj(llon, llat)
plt.contourf(lonproj, latproj, T_CTRL, levels=np.arange(8,30,1))
plt.colorbar()

# add solid contour lines
CS = plt.contour(lonproj, latproj, T_CTRL, levels=np.arange(8,30,1), colors='k')

# label contours
plt.clabel(CS, inline=1, fontsize=10, manual=True) # ESC to end selection

# Map T_CTRL - added velocity vectors
plt.clf()
proj = bm.Basemap(projection='merc', llcrnrlat=-50, llcrnrlon=145, urcrnrlat=-20, urcrnrlon=180, resolution='i')
proj.drawcoastlines()
proj.drawparallels([-50,-45,-40,-35,-30,-25,-20], labels=[True,False,False,False])
proj.drawmeridians(range(145,180+1,5), labels=[False,False,False,True])
lonproj, latproj = proj(llon, llat)
plt.contourf(lonproj, latproj, T_CTRL, levels=np.arange(8,30,1))
plt.colorbar()
#
d = 5 # Only plot every dth point in lat and lon
plt.quiver(lonproj[0:-1:d,0:-1:d], latproj[0:-1:d,0:-1:d], U_CTRL[0:-1:d,0:-1:d], V_CTRL[0:-1:d,0:-1:d], scale=10)
#


#
# Bathymetry
#

# Load bathymetry data
bathy = data['bathy']

# Bathymetric contours of interest (where to draw the contours)
isobars = [0,200,500,1000,1500,2000,2500,3000,3500,4000,5000]

# Nice bathymetry map
plt.clf()
proj = bm.Basemap(projection='merc', llcrnrlat=-50, llcrnrlon=145, urcrnrlat=-20, urcrnrlon=180, resolution='i')
proj.drawcoastlines()
proj.drawparallels([-50,-45,-40,-35,-30,-25,20], labels=[True,False,False,False])
proj.drawmeridians(range(145,180+1,5), labels=[False,False,False,True])
lonproj, latproj = proj(llon, llat)
plt.contourf(lonproj, latproj, bathy, levels=isobars, cmap=plt.cm.RdYlBu)
cbar = plt.colorbar()
cbar.set_ticks(isobars)
cbar.set_label('Depth [m]')

#
# Subplots
#

# Temperature change and bathymetry
plt.figure(figsize=(14,5))

plt.subplot(1,2,1)
proj = bm.Basemap(projection='merc', llcrnrlat=-50, llcrnrlon=145, urcrnrlat=-20, urcrnrlon=180, resolution='i')
proj.drawcoastlines()
proj.drawparallels([-50,-45,-40,-35,-30,-25,-20], labels=[True,False,False,False])
proj.drawmeridians(range(145,180+1,5), labels=[False,False,False,True])
lonproj, latproj = proj(llon, llat)
plt.contourf(lonproj, latproj, T_A1B-T_CTRL, levels=np.arange(-3,3+0.5,0.5),  cmap=plt.cm.RdBu_r)
cbar = plt.colorbar()
cbar.set_label(r'SST [$^\circ$C]')

plt.subplot(1,2,2)
proj = bm.Basemap(projection='merc', llcrnrlat=-50, llcrnrlon=145, urcrnrlat=-20, urcrnrlon=180, resolution='i')
proj.drawcoastlines()
proj.drawparallels([-50,-45,-40,-35,-30,-25,20], labels=[True,False,False,False])
proj.drawmeridians(range(145,180+1,5), labels=[False,False,False,True])
lonproj, latproj = proj(llon, llat)
plt.contourf(lonproj, latproj, bathy, levels=isobars, cmap=plt.cm.RdYlBu)
cbar = plt.colorbar()
cbar.set_ticks(isobars)
cbar.set_label('Depth [m]')
