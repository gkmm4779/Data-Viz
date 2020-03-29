#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from sqlalchemy import create_engine


# In[6]:


#connect to sqlite db
db_file= r'C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\gradedata.db'
engine= create_engine(r"sqlite:///{}".format(db_file))
sql= 'SELECT * from test'
'where Grades in (76, 77, 78)'
sales_data_df= pd.read_sql(sql, engine)
sales_data_df


# In[13]:


import pandas as pd
from sqlalchemy import create_engine
#connect to sqlite db
db_file= r'C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\salesdata.db'
engine= create_engine(r"sqlite:///{}".format(db_file))
sql= "select name from sqlite_master"
"where type= 'table';"
sales_data_df= pd.read_sql(sql, engine)
sales_data_df


# In[14]:


sql= "select * from test;"


# In[15]:


sales_data_df


# In[16]:


import pandas as pd
from sqlalchemy import create_engine
#connect to sqlite db
db_file= r'C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\datasets\\salesdata.db'
engine= create_engine(r"sqlite:///{}".format(db_file))
sql= "select name from sqlite_master"
"where type= 'name';"
sales_data_df= pd.read_sql(sql, engine)
sales_data_df

