
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:15:46 2019
@author: y56
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = pd.read_csv('/Users/y56/Desktop/train.csv')
#%%
df.head()
#%%
df.info()
#%%
df.describe()
#%%
df.isnull().sum()
#%%
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#%%
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=df,palette='RdBu_r')
#%%
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=df,palette='RdBu_r')
#%%
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=df,palette='rainbow')
#%%
sns.distplot(df['Age'].dropna(),kde=False,color='darkred',bins=30)
#%%
df['Age'].hist(bins=30,color='darkred',alpha=0.7)
#%%
sns.countplot(x='SibSp',data=df)
#%%
df['Fare'].hist(color='green',bins=40,figsize=(8,4))
#%%
import cufflinks as cf
cf.go_offline()
#%%
df['Fare'].iplot(kind='hist',bins=30,color='green')
#%%
plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=df,palette='winter')
#%%
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age
#%%
df['Age'] = df[['Age','Pclass']].apply(impute_age,axis=1)
#%%
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#%%
df.drop('Cabin',axis=1,inplace=True)
#%%
df.head()
#%%
df.dropna(inplace=True)
#%%
sex = pd.get_dummies(df['Sex'],drop_first=True)
embark = pd.get_dummies(df['Embarked'],drop_first=True)
#%%
df.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
#%%
df = pd.concat([df,sex,embark],axis=1)
#%%
df.head()
#%%
from sklearn.model_selection import train_test_split
#%%
X_train, X_test, y_train, y_test = train_test_split(df.drop('Survived',axis=1), 
                                                    df['Survived'], test_size=0.30, 
                                                    random_state=101)
#%%
from sklearn.linear_model import LogisticRegression
#%%
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
#%%
predictions = logmodel.predict(X_test)
#%%
from sklearn.metrics import classification_report
#%%
print(classification_report(y_test,predictions))
#%%
from sklearn.metrics import confusion_matrix
#%%
confusion_matrix(y_test,predictions)
#%%
