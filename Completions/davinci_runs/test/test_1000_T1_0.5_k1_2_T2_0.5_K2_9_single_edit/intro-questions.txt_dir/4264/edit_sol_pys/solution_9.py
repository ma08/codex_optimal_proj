#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv('kyphosis.csv')


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


sns.pairplot(df,hue='Kyphosis',palette='Set1')


# In[11]:


from sklearn.cross_validation import train_test_split


# In[12]:


X = df.drop('Kyphosis',axis=1)


# In[13]:


y = df['Kyphosis']


# In[14]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


# In[15]:


from sklearn.tree import DecisionTreeClassifier


# In[16]:


dtree = DecisionTreeClassifier()


# In[17]:


dtree.fit(X_train,y_train)


# In[18]:


predictions = dtree.predict(X_test)


# In[19]:


from sklearn.metrics import classification_report,confusion_matrix


# In[20]:


print(classification_report(y_test,predictions))


# In[21]:


print(confusion_matrix(y_test,predictions))


# In[22]:


from sklearn.ensemble import RandomForestClassifier


# In[23]:


rfc = RandomForestClassifier(n_estimators=200)


# In[24]:


rfc.fit(X_train, y_train)


# In[25]:


rfc_pred = rfc.predict(X_test)


# In[26]:


print(classification_report(y_test,rfc_pred))


# In[27]:


print(confusion_matrix(y_test,rfc_pred))


# In[ ]:






N = int(input())

count = 0
for i in range(1, N+1):
    count += len(str(i)) % 2

print(count)
