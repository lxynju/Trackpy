# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:59:50 2023

@author: dell
"""

import pandas as pd
from pandas import DataFrame, Series

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('circularMotionData.csv')
df['x'] = pd.to_numeric(df['x'])
df['y'] = pd.to_numeric(df['y'])
df['x'] = df['x'] - (df['x'].max() + df['x'].min())/2
df['y'] = df['y'] - (df['y'].max() + df['y'].min())/2 
#par0 = df.loc[df['particle'] == 0]
par1 = df.loc[df['particle'] == 1]
par1[['x','y']].plot()

df = pd.read_csv('circularMotionData.csv')
df['x'] = pd.to_numeric(df['x'])
df['y'] = pd.to_numeric(df['y'])
par0 = df.loc[df['particle'] == 0]
par1 = df.loc[df['particle'] == 1]

plt.figure()
plt.plot(np.arctan2(par1['y'].values - par0['y'].values, par1['x'].values - par0['x'].values))