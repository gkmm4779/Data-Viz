#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[2]:


#Create bin dividers
bins= [0, 60, 70, 80, 90, 100]
#create names for the 4 groups
group_names= ['F', 'D', 'C', 'B', 'A']


# In[3]:


df['lettergrade']= pd.cut(df['grade'], bins, labels= group_names)
df


# In[5]:


pd.value_counts(df['lettergrade'])


# In[6]:


import pandas as pd
Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[12]:


#Create bin dividers
bins= [79, 80, 100]
#create names for the 4 groups
group_names= ['Fail', 'Pass']


# In[13]:


df['Pass/Fail']= pd.cut(df['grade'], bins, labels= group_names)
df


# In[ ]:




