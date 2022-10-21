# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

import numpy as np

from astropy.io import ascii


x=2+2

#plot= plt.axes()
#import astropy.units as u
#plot= plt.axes()

data='/c/Users/Farhan/Downloads/Tutorial_IV/'
new_data=data+'example_python.py'


xs = np.arange(-10,10.01,0.01)



def gaussian(xs,a,mu,sigma):
    xs = np.arange(-10,10.01,0.01)
    a=4.5
    mu=3.5
    sigma=2.2
    ys = a/np.sqrt(2*np.pi)*np.exp(-(xs-mu)**2/(2*sigma**2))
    
    return ys
y=gaussian(xs,4.5,3.5,2.2)

#print(y)

plt.plot(xs,y,c='red',ls='--')








    

