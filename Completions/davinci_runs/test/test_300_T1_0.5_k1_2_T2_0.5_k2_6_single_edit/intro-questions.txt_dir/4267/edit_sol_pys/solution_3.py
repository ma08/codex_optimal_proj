
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:42:01 2018
@author: rajiv
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = pd.read_csv('data/train.csv')
print(df.head())
#%%
df.info()
#%%
print(df.describe())
