#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[2]:


df=df.sort_values(by='age', ascending=0)
df.head()


# In[3]:


df=df.sort_values(by=['grade', 'age'], ascending=[True, True])
df.head()


# In[5]:


df=df.sort_values(by=['fname','lname', 'grade', 'age'], ascending=[True, True, True, True])
df.head()


# In[ ]:




