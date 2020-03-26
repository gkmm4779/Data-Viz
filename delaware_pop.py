#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[8]:


Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\delaware census.csv"


# In[9]:


df= pd.read_csv(Location, header=None)


# In[10]:


df.head()


# In[11]:


import pandas as pd


# In[16]:


Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\delawarecensus.csv"


# In[17]:


#to add headers as we load the data
df= pd.read_csv(Location, names=['Pop','Name'])


# In[19]:


df.head()

