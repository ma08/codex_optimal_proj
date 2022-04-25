#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:03:23 2019

@author: alexander
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/train.csv')

#df.head()

#df.describe()

#df.info()

#df.hist(figsize=(20,15))

#df['SalePrice'].plot(kind='hist')

plt.figure(figsize=(15,10))
plt.scatter(df['LotArea'], df['SalePrice'])
plt.show()
