#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
all_data= pd.DataFrame()


# In[7]:


import pandas as pd
import numpy as np
all_data=pd.DataFrame()
df=pd.read_excel("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data1.xlsx")
all_data=all_data.append(df, ignore_index= True)
df=pd.read_excel("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data2.xlsx")
all_data= all_data.append(df, ignore_index= True)
df=pd.read_excel("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data3.xlsx")
all_data=all_data.append(df, ignore_index= True)
all_data.describe()


# In[9]:


import pandas as pd
import numpy as np
all_data=pd.DataFrame()
df=pd.read_excel("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data1.xlsx")
all_data=all_data.append(df, ignore_index= True)
df=pd.read_excel("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data2.xlsx")
all_data= all_data.append(df, ignore_index= True)
df=pd.read_excel("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data3.xlsx")
all_data=all_data.append(df, ignore_index= True)
all_data.describe()


# In[17]:


import pandas as pd
import numpy as np
import glob
all_data=pd.DataFrame()
for f in glob.glob("C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\data*.xlsx"):
    df=pd.read_excel(f)
all_data=all_data.append(df, ignore_index= True)
all_data.describe()


# In[27]:


import pandas as pd
import numpy as np
import glob
all_data= pd.DataFrame()
for f in glob.glob("C:\\Users\\gkmm4\\OneDrive\\Documents\\datasets\\weekly_call_data*.xlsx"):
    df= pd.read_excel(f)
    all_data= all_data.append(df, ignore_index= True)
    all_data.describe()


# In[ ]:




