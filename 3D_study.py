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
#select and copy the column
plotdata = data.iloc[:,4:7].copy()
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(plotdata.iloc[:,0], plotdata.iloc[:,1], plotdata.iloc[:,2])
plt.show()

scatter(plotdata[:,0], plotdata[:,1], plotdata[:,2])