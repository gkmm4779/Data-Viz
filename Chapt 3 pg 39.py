#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
Location= "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[15]:


import numpy as np
df['isBusy']= np.where((df['exercise']>3) & (df['hours']>17), 'yes', 'no')
df.tail(10)

