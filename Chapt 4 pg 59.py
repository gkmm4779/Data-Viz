#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names= ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades= [76,95,77, 78,99]
bs=[1,1,0,0,1]
ms=[2,1,0,0,0]
phd=[0,1,0,0,0]
Gradelist= zip(names, grades, bs, ms, phd)
df= pd.DataFrame(data=Gradelist, columns=['Names', 'Grades','BS', 'MS', 'PhD'])
df


# In[2]:


df.loc[df['MS']==0]['Grades'].mean()


# In[ ]:




