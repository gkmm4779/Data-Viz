#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
names= ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
absences= [3,0,1,0,8]
detentions=[2,1,0,0,1]
warnings=[2,1,5,1,2]
Gradelist= zip(names, absences, detentions, warnings)
df= pd.DataFrame(data=Gradelist, columns= ['Names', 'Absences', 'Detentions', 'Warnings'])
get_ipython().run_line_magic('matplotlib', 'inline')
df


# In[4]:


df['TotalDemerits']=df['Absences']+df['Detentions']+df['Warnings']
df


# In[5]:


plt.pie(df['TotalDemerits'])


# In[24]:


plt.pie(df['TotalDemerits'], 
        labels=df['Names'],
       explode=(0,0,0,0,0.15),
       startangle=90,
       autopct='%1.1f%%',)
plt.axis('equal')


# In[30]:


plt.pie(df['TotalDemerits'], 
        labels=df['Names'],
       explode=(0,0,0,0.5,0),
       startangle=180,
       autopct='%1.1f%%',)
plt.axis('equal')


# In[ ]:




