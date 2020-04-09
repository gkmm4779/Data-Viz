#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[7]:


def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0
df['gender_val']=df['gender'].apply(score_to_numeric)
df.tail()


# In[8]:


import statsmodels.formula.api as sm
result= sm.ols(formula='grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()

