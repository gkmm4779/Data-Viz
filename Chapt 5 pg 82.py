#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[3]:


df.hist()


# In[4]:


df.hist(column='hours')


# In[5]:


df.hist(column='hours', by='gender')


# In[7]:


df.hist(column='age', by='gender')


# In[ ]:




