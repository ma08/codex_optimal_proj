
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:34:27 2019
@author: nidhi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
data=pd.read_csv('/Users/nidhi/Desktop/knn/diabetes.csv')
data.head()
data.info()
data.describe()
data.isnull().sum()
data.corr()
sns.heatmap(data.corr(),annot=True)
sns.pairplot(data)
sns.countplot(x='Outcome',data=data)
sns.countplot(x='Pregnancies',data=data)
sns.countplot(x='Glucose',data=data)
sns.countplot(x='BloodPressure',data=data)
sns.countplot(x='SkinThickness',data=data)
sns.countplot(x='Insulin',data=data)
sns.countplot(x='BMI',data=data)
sns.countplot(x='DiabetesPedigreeFunction',data=data)
sns.countplot(x='Age',data=data)
x=data.iloc[:,0:8]
y=data.iloc[:,8]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
classifier=KNeighborsClassifier(n_neighbors=11,p=2,metric='euclidean')
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
cm=confusion_matrix(y_test,y_pred)
print(cm)
print(f1_score(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
