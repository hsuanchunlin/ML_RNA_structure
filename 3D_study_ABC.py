# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:49:04 2018
Study 3D plot
@author: fatmi
"""
import matplotlib as mpl
import pandas as pd
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("21ABC rk ave summary-U.csv")

cmap = plt.cm.hsv
#select and copy the column
plotdata = data.iloc[:,1:4].copy()
colors = np.abs(data.iloc[:,6].copy())
mpl.rcParams['legend.fontsize'] = 10
figure = plt.figure()
ax1 = figure.gca(projection = '3d')
ax1.scatter(np.log(plotdata.iloc[:,0]),np.log(plotdata.iloc[:,1]),
            np.log(plotdata.iloc[:,2]), s = 1, c= colors, cmap = cmap)
plt.show()
np.max(np.log(plotdata.iloc[:,2]))
np.min(np.log(plotdata.iloc[:,2]))