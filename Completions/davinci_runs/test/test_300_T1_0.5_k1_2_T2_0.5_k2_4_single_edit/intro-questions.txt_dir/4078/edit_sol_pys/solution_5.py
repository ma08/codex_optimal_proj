
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# In[2]:


dataset = pd.read_csv('dataset.csv')
dataset.head()


# In[3]:


dataset.drop(['Name','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
dataset.head()


# In[4]:


dataset.isnull().sum()


# In[5]:


mean = dataset['Age'].mean()
dataset['Age'].fillna(mean,inplace=True)
mean = dataset['Fare'].mean()
dataset['Fare'].fillna(mean,inplace=True)
dataset.isnull().sum()


# In[6]:


dataset.drop(['PassengerId'],axis='columns',inplace=True)
dataset.head()


# In[7]:


inputs = dataset.drop(['Survived'],axis='columns')
target = dataset['Survived']


# In[8]:


inputs.head()


# In[9]:


target.head()


# In[10]:


X_train,X_test,y_train,y_test = train_test_split(inputs,target,test_size=0.2)


# In[11]:


model = RandomForestClassifier(n_estimators=100)


# In[12]:


model.fit(X_train,y_train)


# In[13]:


model.score(X_test,y_test)


# In[ ]:



