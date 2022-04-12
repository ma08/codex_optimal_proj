#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:14:09 2020
@author: ritambasu
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
#function that returns dy/dt
def model(y,t):
    k=0.3
    dydt= -k*y
    return dydt
#initial condition
y0=5
#time points
t=np.linspace(0,20)
#solve ODE
y=odeint(model,y0,t)
#plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
