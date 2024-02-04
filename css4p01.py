#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
df = pd.read_csv('E:\CSS-2024\data_01\data_01\movie_dataset.csv')
df.dropna(subset=['Metascore'], inplace=True) 
df.dropna(subset=['Revenue (Millions)'], inplace=True)
#df.fillna(method='ffill', inplace=True)


# In[36]:


df.head()


# In[43]:


df.loc[df['Rating']==df['Rating'].max()]


# In[44]:


df["Revenue (Millions)"].sum()


# In[47]:


year_2015_2017 = df[(df["Year"]>=2015) & (df["Year"]<=2017)]


# In[48]:


year_2015_2017


# In[50]:


year_2015_2017["Revenue (Millions)"].mean()


# In[56]:


frame = pd.read_csv('E:\CSS-2024\data_01\data_01\movie_dataset.csv')
movies_year_2016 = frame[frame["Year"]==2016]
movies_year_2016


# Movies_year_2016

# In[57]:


number_movies_2016 = len(movies_year_2016)
number_movies_2016


# In[58]:


directed_by_nolan_c = frame[frame['Director']=="Christopher Nolan"]
len(directed_by_nolan_c)


# In[59]:


rating_atleast_8 = len(frame[frame['Rating']>=8.0])
rating_atleast_8


# In[64]:


#directed_by_nolan_c.dropna(subset=['Rating'], inplace=True)
median=directed_by_nolan_c["Rating"].median()


# In[65]:


median


# In[83]:


frame.groupby('Year')['Revenue (Millions)'].mean()


# In[82]:


frame.groupby('Year')['Rating'].min()


# In[81]:


(1911.7-313.5)/313.5*100
actors = [frame.Actors]
actors


# In[78]:



# In[ ]:




