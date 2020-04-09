#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
names= ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades= [76,83,77,78,95]
Gradelist= zip(names, grades)
df= pd.DataFrame(data=Gradelist, columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[4]:


df.plot()
displayText= "my annotation"
xloc=1
yloc=df['Grades'].max()
xtext=8
ytext=0
plt.annotate(displayText, xy=(xloc, yloc), xytext=(xtext, ytext), xycoords=('axes fraction', 'data'), textcoords='offset points')


# In[6]:


df.plot()
displayText= "my annotation"
xloc=1
yloc=df['Grades'].max()
xtext=8
ytext=-150
plt.annotate(displayText, xy=(xloc, yloc), arrowprops=dict(facecolor='black', shrink=0.05),xytext=(xtext, ytext), xycoords=('axes fraction', 'data'), textcoords='offset points')


# In[16]:


df.plot()
displayText= "Wow"
xloc=1
yloc=df['Grades'].min()
xtext=0
ytext=0
plt.annotate(displayText, xy=(xloc, yloc), arrowprops=dict(facecolor='black', shrink=0.05),xytext=(xtext, ytext), xycoords=('axes fraction', 'data'), textcoords='figure fraction')


# In[ ]:




