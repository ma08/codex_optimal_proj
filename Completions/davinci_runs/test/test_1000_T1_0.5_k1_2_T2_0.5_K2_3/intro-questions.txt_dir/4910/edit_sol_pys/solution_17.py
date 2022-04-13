#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:07:11 2019

@author: kendalljohnson
"""

# Title - A program to make a histogram of a dataset

# Imports :: modules used to create code

import numpy as np
import matplotlib.pyplot as plt

# Data :: 

Data = np.loadtxt('Data.txt')

# Creating a histogram

plt.hist(Data, bins = 10, color = 'green')

# Labels

plt.xlabel('Data Value')
plt.ylabel('Frequency')
plt.title('Data Histogram')

# Showing the plot

plt.show()
