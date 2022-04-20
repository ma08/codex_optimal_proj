#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("C:/Users/Dell/Desktop/ML/ML/train.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


df.isnull().sum()


# In[8]:


df.shape


# In[9]:


df['Age'].hist(bins=20)


# In[10]:


df['Age'].isnull().sum()


# In[11]:


df['Age'].fillna(df['Age'].mean(),inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


df['Embarked'].value_counts()


# In[14]:


df['Embarked'].fillna('S',inplace=True)


# In[15]:


df.isnull().sum()


# In[16]:


df.drop('Cabin',axis=1,inplace=True)


# In[17]:


df.isnull().sum()


# In[18]:


df.drop('PassengerId',axis=1,inplace=True)


# In[19]:


df.isnull().sum()


# In[20]:


df.drop('Name',axis=1,inplace=True)


# In[21]:


df.isnull().sum()


# In[22]:


df.drop('Ticket',axis=1,inplace=True)


# In[23]:


df.isnull().sum()


# In[24]:


df.head()


# In[25]:


df['Sex'].value_counts()


# In[26]:


df['Sex']=df['Sex'].map({'male':0,'female':1})


# In[27]:


df.head()


# In[28]:


df['Embarked'].value_counts()


# In[29]:


df['Embarked']=df['Embarked'].map({'S':0,'C':1,'Q':2})


# In[30]:


df.head()


# In[31]:


df.info()


# In[32]:


df.drop('Survived',axis=1,inplace=True)


# In[33]:


df.info()


# In[34]:


df.head()


# In[35]:


y=df['Survived']


# In[36]:


df.drop('Survived',axis=1,inplace=True)


# In[37]:


df.head()


# In[38]:


from sklearn.model_selection import train_test_split


# In[39]:


X_train,X_test,y_train,y_test=train_test_split(df,y,test_size=0.3,random_state=0)


# In[40]:


from sklearn.linear_model import LogisticRegression


# In[41]:


logreg=LogisticRegression()


# In[42]:


logreg.fit(X_train,y_train)


# In[43]:


y_pred=logreg.predict(X_test)


# In[44]:


from sklearn.metrics import confusion_matrix


# In[45]:


confusion_matrix(y_test,y_pred)


# In[46]:


from sklearn.metrics import classification_report


# In[47]:


print(classification_report(y_test,y_pred))


# In[48]:


from sklearn.metrics import accuracy_score


# In[49]:


accuracy_score(y_test,y_pred)


# In[50]:


from sklearn.metrics import roc_auc_score


# In[51]:


roc_auc_score(y_test,y_pred)


# In[52]:


from sklearn.metrics import roc_curve


# In[53]:


y_pred_proba=logreg.predict_proba(X_test)[:,1]


# In[54]:


fpr,tpr,thresholds=roc_curve(y_test,y_pred_proba)


# In[55]:


plt.plot([0,1],[0,1],'k--')
plt.plot(fpr,tpr,label='Logistic Regression')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




n = int(input())
f = [int(x) for x in input().split()]

# Find friends who don't know who to give gifts to
# and friends who don't know who gives them gifts
no_gift_to = []
no_gift_from = []
for i in range(n):
    if f[i] == 0:
        no_gift_to.append(i)
    else:
        if f[f[i] - 1] == 0:
            no_gift_from.append(f[i] - 1)

# Give gifts to friends who don't know who gives them gifts
for i in range(len(no_gift_to)):
    f[no_gift_from[i]] = no_gift_to[i] + 1

# Give gifts to friends who don't know who to give gifts to
for i in range(len(no_gift_to)):
    f[no_gift_to[i]] = no_gift_from[i] + 1

print(" ".join(str(x) for x in f))
