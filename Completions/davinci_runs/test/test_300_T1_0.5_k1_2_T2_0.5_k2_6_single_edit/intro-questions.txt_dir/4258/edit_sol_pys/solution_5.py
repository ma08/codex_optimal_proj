#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("data/gapminder.tsv", sep='\t')
df.head()


# In[3]:


df.columns


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.columns


# In[8]:


df.columns = ['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap']


# In[9]:


df.head()


# In[10]:


df.loc[0]


# In[11]:


df.iloc[0]


# In[12]:


df.loc[99]


# In[13]:


df.iloc[99]


# In[14]:


df.loc[-1]


# In[15]:


df.iloc[-1]


# In[16]:


df.loc[0:99]


# In[17]:


df.iloc[0:99]


# In[18]:


df.head()


# In[19]:


df.loc[0]


# In[20]:


df.loc[0:4]


# In[21]:


df.iloc[0:4]


# In[22]:


df.loc[0:4, 'country']


# In[23]:


df.iloc[0:4, 0]


# In[24]:


df.iloc[:, 0]


# In[25]:


df.iloc[:, 0:4]


# In[26]:


df.iloc[:, :4]


# In[27]:


df.iloc[:, [0, 2, 4]]


# In[28]:


df.iloc[:, [0, 2, -1]]


# In[29]:


df.head()


# In[30]:


df.loc[:, ['year', 'pop']]


# In[31]:


df.iloc[:, [2, 4]]


# In[32]:


df.iloc[[0, 99, 999], [0, 3, 5]]


# In[33]:


df.head()


# In[34]:


df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']]


# In[35]:


df.iloc[10:13, [0, 3, 5]]


# In[36]:


df.head()


# In[37]:


df.loc[df['country'] == 'United States']


# In[38]:


df.loc[df['country'] == 'United States'].iloc[:, [0, 1, 3, 5]]


# In[39]:


df.loc[df['country'] == 'United States'].iloc[:, [0, 1, 3, 5]].head()


# In[40]:


df.loc[df['country'] == 'United States'].iloc[:, [0, 1, 3, 5]].tail()


# In[41]:


df.loc[df['country'] == 'United States'].iloc[:, [0, 1, 3, 5]].describe()


# In[42]:


df.loc[df['country'] == 'Argentina']


# In[43]:


df.loc[df['country'] == 'Argentina'].iloc[:, [0, 1, 3, 5]]


# In[44]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]]


# In[45]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe()


# In[46]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['min']


# In[47]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['max']


# In[48]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['mean']


# In[49]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['std']


# In[50]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['25%']


# In[51]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['50%']


# In[52]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['75%']


# In[53]:


df.loc[(df['country'] == 'Argentina') | (df['country'] == 'United States')].iloc[:, [0, 1, 3, 5]].describe().loc['count']


# In[ ]:



