#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location="C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\04-01-2020.csv"
df= pd.read_csv(Location)
df.head()


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data= pd.read_csv("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\04-01-2020.csv")
plot_data= data['Confirmed'].sum()
sns.lineplot(plot_data.index, plot_data, color= 'yellow')
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.title("Confirmed Cases in US")
plt.show()


# In[ ]:




