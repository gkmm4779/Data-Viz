#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
names= ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades= [76,95,77,78,99]
status=['Senior', 'Freshman','Sophomore', 'Senior', 'Junior']
Gradelist= zip(names, grades, status)
df= pd.DataFrame(data=Gradelist, columns=['Names', 'Grades', 'Status'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[7]:


df2=df.set_index(df['Status'])
df2.plot(kind='bar')


# In[ ]:




