#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:37:33 2020

@author: abhijithneilabraham
"""

import os
os.getcwd()
os.chdir('/Users/abhijithneilabraham/Downloads')
os.getcwd()
import pandas as pd
df=pd.read_csv('/Users/abhijithneilabraham/Downloads/train.csv')
df.head()
df.describe()
df.info()
df.shape
df.columns
df.isnull().sum()
df.isnull().sum().sum()
df.isnull().sum().sum()/df.shape[0]
df.isnull().sum().sum()/df.shape[0]*100
df.shape[0]
df.shape[1]
df.shape[0]*df.shape[1]
len(df.columns)
len(df.index)
df.columns.tolist()
df.index.tolist()
df.dtypes
df.dtypes.value_counts()
df.dtypes.value_counts().plot(kind='bar')
import matplotlib.pyplot as plt
df.dtypes.value_counts().plot(kind='bar')
plt.show()
df.dtypes.value_counts().plot(kind='bar')
plt.show()
df.dtypes.value_counts().plot(kind='pie')
plt.show()
df.dtypes.value_counts().plot(kind='bar')
plt.show()
df.dtypes.value_counts().plot(kind='pie')
plt.show()
df.dtypes.value_counts().plot(kind='barh')
plt.show()
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.jpg')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.svg')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.pdf')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=300)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=1000)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=2000)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='portrait')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5,frameon=True)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5,frameon=True,metadata=None)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5,frameon=True,metadata=None,bbox_extra_artists=None)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5,frameon=True,metadata=None,bbox_extra_artists=None,bbox_inches='tight')
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5,frameon=True,metadata=None,bbox_extra_artists=None,bbox_inches='tight',)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.png',dpi=500,bbox_inches='tight',transparent=True,facecolor='red',edgecolor='blue',orientation='landscape',papertype='legal',format='png',pad_inches=0.5,frameon=True,metadata=None,bbox_extra_artists=None,bbox_inches='tight',)
df.dtypes.value_counts().plot(kind='barh')
plt.savefig('plot.
