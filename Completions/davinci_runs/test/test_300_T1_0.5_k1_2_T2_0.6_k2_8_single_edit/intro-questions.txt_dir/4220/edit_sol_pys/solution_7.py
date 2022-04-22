#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('kyphosis.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


sns.pairplot(df,hue='Kyphosis',palette='Set1')


# In[6]:


from sklearn.cross_validation import train_test_split


# In[7]:


X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


# In[9]:


from sklearn.tree import DecisionTreeClassifier


# In[10]:


dtree = DecisionTreeClassifier()


# In[11]:


dtree.fit(X_train,y_train)


# In[12]:


predictions = dtree.predict(X_test)


# In[13]:


from sklearn.metrics import classification_report,confusion_matrix


# In[14]:


print(classification_report(y_test,predictions))


# In[15]:


print(confusion_matrix(y_test,predictions))


# In[16]:


from sklearn.ensemble import RandomForestClassifier


# In[17]:


rfc = RandomForestClassifier(n_estimators=100)


# In[18]:


rfc.fit(X_train, y_train)


# In[19]:


rfc_pred = rfc.predict(X_test)


# In[20]:


print(confusion_matrix(y_test,rfc_pred))


# In[21]:


print(classification_report(y_test,rfc_pred))


# In[ ]:






K = int(input())
S = input()

if len(S) > K:
    print(S[:K] + '...')
else:
    print(S)
