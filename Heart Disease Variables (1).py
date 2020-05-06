#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
import scipy.stats as st
from sklearn.ensemble import RandomForestClassifier #for the model
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz #plot tree
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:\\Users\\gkmm4\\OneDrive\\Documents\\Data Viz\\heart.csv"
df_heart = pd.read_csv(Location)
df_heart.head(10)


# In[5]:


print('Descriptive Statistics\n')
df_heart.describe()


# In[9]:


df_heart['target'].value_counts()


# In[78]:


f, ax = plt.subplots(figsize=(8,6))
ax = sns.countplot(x="target", palette= 'Blues', edgecolor='black', data=df_heart)
plt.xlabel('0=No Heart Disease, 1=Heart Disease', fontsize='large', fontweight='bold')
plt.ylabel('Count',fontsize='large', fontweight='bold')
plt.title('Count of Presence or Absence of Heart Disease',fontsize='large', fontweight='bold')
plt.show()


# In[18]:


f, ax = plt.subplots(figsize=(8, 6))
ax = sns.countplot(x="sex", palette= 'Blues',edgecolor='black', data= df_heart)
plt.xlabel('0=Female, 1=Male', fontsize='large', fontweight='bold')
plt.ylabel('Count',fontsize='large', fontweight='bold')
plt.title('Count of Female/Male, With Heart Disease',fontsize='large', fontweight='bold')
plt.show()


# In[17]:


f, ax = plt.subplots(figsize=(8, 6))
ax = sns.countplot(x="sex", hue= "target", palette= 'Blues',edgecolor='black', data= df_heart)
plt.xlabel('0=Female, 1=Male', fontsize='large', fontweight='bold')
plt.ylabel('Count',fontsize='large', fontweight='bold')
plt.title('Count of Female/Male, Without and With Heart Disease',fontsize='large', fontweight='bold')
plt.show()


# In[55]:


# create figure and axis
fig, ax = plt.subplots(figsize= (20,10))
# plot histograms
ax.hist(df_heart['age'], color= 'seagreen', edgecolor='black')
# set title and labels
ax.set_title('Age Distribution of Dataset', fontsize='large', fontweight='bold')
ax.set_xlabel('Age',fontsize='large', fontweight='bold')
ax.set_ylabel('Frequency',fontsize='large', fontweight='bold')


# In[70]:


fig, ax = plt.subplots(figsize= (20,10))
# plot histogram
ax.hist(df_heart['cp'], color= 'seagreen')
# set title and labels
ax.set_title('CP', fontsize='large', fontweight='bold')
ax.set_xlabel('CP', fontsize='large', fontweight='bold')
ax.set_ylabel('Frequency',fontsize='large', fontweight='bold')


# In[87]:


# Heatmap of Heart disease variable weights 
fig = plt.figure(figsize=(20,10))
sns.heatmap(df_heart.corr(), cmap='Blues',fmt='.2f',linewidths=2, annot= True)


# In[72]:


corr = df_heart.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))

sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,mask=mask,cmap='BuGn',edgecolor='black', vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# In[65]:


import scipy as scipy
from scipy.cluster import hierarchy as hc


# In[66]:


def hierarchy_tree(df):
    corr = np.round(scipy.stats.spearmanr(df_heart).correlation, 4)
    corr_condensed = hc.distance.squareform(1-df.corr())
    z = hc.linkage(corr_condensed, method='average')
    fig = plt.figure(figsize=(16,10))
    dendrogram = hc.dendrogram(z, labels=df.columns, orientation='left', leaf_font_size=16)
    plt.show()


# In[67]:


hierarchy_tree(df_heart)


# In[80]:


fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(1, 3, 1)
age_bins = [20,30,40,50,60,70,80]
df_heart['bin_age']=pd.cut(df_heart['age'], bins=age_bins)
g1=sns.countplot(x='bin_age',data=df_heart,hue='target',palette='Blues', edgecolor='black', linewidth=2)
g1.set_title("Age vs Heart Disease",fontsize='large', fontweight='bold' )
#The highest number of people with heart disease are between the age 41-55


# In[81]:


fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(1, 3, 2)
cho_bins = [100,150,200,250,300,350,400,450]
df_heart['bin_chol']=pd.cut(df_heart['chol'], bins=cho_bins)
g2=sns.countplot(x='bin_chol',data=df_heart,hue='target',palette='Blues', edgecolor='black', linewidth=2)
g2.set_title("Cholestoral levels and Risk of Heart Disease", fontsize='large', fontweight='bold')
#people with 200-250 cholestrol have a higher incidence of heart disease 


# In[19]:


fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(131)
x1=sns.countplot(x='cp',data=df_heart,hue='target',palette='Blues',edgecolor='black', linewidth=2)
plt.xlabel('0=typical angina, 1=atypical angina,2=non-anginal pain, 3=no chest pain',fontsize='large', fontweight='bold')
x1.set_title('Chest pain type and Risk of Heart Disease',fontsize='large', fontweight='bold')
#Chest pain type 2 has the highest incidence of heart disease


# In[66]:


fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(133)
x3=sns.countplot(x='slope',data=df_heart,hue='target',palette='BuGn',edgecolor='black', linewidth=2)
plt.xlabel('1=upsloping, 2=flat, 3=downsloping',fontsize='large', fontweight='bold')
x3.set_title('Slope of the peak exerciseand ST segment', fontsize='large', fontweight='bold')
#Slope 2 has the highest incidence of heart disease


# In[83]:


fig,ax=plt.subplots(figsize=(30,6))
plt.subplot(1, 3, 2)
trestbps_bins = [130, 140, 150, 160, 170, 180, 190, 200]
df_heart['bin_trestbps']=pd.cut(df_heart['chol'], bins=trestbps_bins)
g2=sns.countplot(x='bin_trestbps',data=df_heart,hue='target',palette='Blues', edgecolor='black', linewidth=2)
g2.set_title("Resting Blood Pressure vs Heart Disease", fontsize='large', fontweight='bold')


# In[85]:


fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(131)
x1=sns.countplot(x='exang',data=df_heart,hue='target',palette='Blues', edgecolor='black', linewidth=2)
x1.set_xlabel('0=No Angina, 1=Angina')
x1.set_title('Exercise Induced Chest Pain and Risk of Heart Disease',fontsize='large', fontweight='bold')


# In[84]:


fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(131)
x1=sns.countplot(x='fbs',data=df_heart,hue='target',palette='Blues', edgecolor='black', linewidth=2)
x1.set_xlabel('0=False, 1=True')
x1.set_title('Fasting Blood Sugar >120 and Risk of Heart Disease',fontsize='large', fontweight='bold')


# In[27]:


sns.lmplot(x="trestbps", y="chol",data=df_heart,hue="cp")
plt.show()


# In[28]:


sns.lmplot(x="trestbps", y="chol",data=df_heart)
plt.show()


# In[ ]:




