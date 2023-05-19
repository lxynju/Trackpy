# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:10:55 2023

@author: dell
"""

import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.rc('figure', figsize = (5,5))
mpl.rc('image', cmap = 'gray')

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import pims
import trackpy as tp

@pims.pipeline
def gray(imag):
    return imag[:, :, 2]

frames = gray(pims.open('fig/*.jpg'))
plt.gca().invert_yaxis()
plt.imshow(frames[0])
f = tp.locate(frames[0], 11, invert=True)
f = f[(f['mass'] > 800) & (f['ecc'] <0.2)]
tp.annotate(f, frames[0]);
f = tp.batch(frames[:], 11, minmass=800, invert=True, processes=1);  # lxy: note without processes = 1, will get error

t = tp.link(f, 10, memory=3)
t1 = tp.filter_stubs(t, 5)
t2 = t1[((t1['mass'] > 800) & (t1['size'] < 5) &
         (t1['ecc'] < 0.2))]
t2.to_csv('circularMotionData.csv', mode='w')
plt.figure()
tp.plot_traj(t2);

