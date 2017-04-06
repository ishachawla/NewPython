
# coding: utf-8

# In[1]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv


# In[21]:

df=pd.read_csv('cricket_matches.csv')


# In[22]:

df=df[df['home']==df['winner']]


# In[23]:


f = {'innings1':['size'],'innings1_runs':['sum']}
df=df.groupby('innings1').agg(f)


# In[24]:

df1=pd.read_csv('cricket_matches.csv')


# In[25]:

df1=df1[df1['home']==df1['winner']]


# In[26]:


f1 = {'innings2':['size'],'innings2_runs':['sum']}
df1=df1.groupby('innings2').agg(f1)


# In[27]:

df=df.merge(df1,how='outer', left_index=True, right_index=True)


# In[29]:

df['Total Runs'] = df.fillna(0)['innings1_runs'] + df.fillna(0)['innings2_runs']
df['Total Innings'] = df.fillna(0)['innings1'] + df.fillna(0)['innings2']


# In[31]:

df['Average']=df['Total Runs']/df['Total Innings']


# In[33]:

df=df.drop('innings1',axis=1)
df=df.drop('innings1_runs',axis=1)
df=df.drop('innings2',axis=1)
df=df.drop('innings2_runs',axis=1)
df=df.drop('Total Runs',axis=1)
df=df.drop('Total Innings',axis=1)


# In[35]:

with open('Q3A1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Team','Average'])


# In[36]:

with open('Q3A1.csv', 'a') as f:
    df.to_csv(f, header=False)


# In[ ]:



