
# coding: utf-8

# In[79]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv


# In[37]:

df=pd.read_csv('vehicle_collisions.csv',parse_dates=['DATE'],infer_datetime_format=True)


# In[38]:

df["Year"] = pd.to_datetime(df["DATE"])


# In[39]:

df=df[(df.BOROUGH =='MANHATTAN') & (df["Year"].dt.year==2016)]


# In[40]:

df=df.groupby([df["Year"].dt.month]).count()


# In[41]:

li=['BOROUGH']


# In[42]:

df=df[li].sum(axis=1)


# In[44]:

df2=pd.read_csv('vehicle_collisions.csv',parse_dates=['DATE'],infer_datetime_format=True)


# In[45]:

df2["Y"] = pd.to_datetime(df2["DATE"])


# In[46]:

df2=df2[(df2["Y"].dt.year==2016)]


# In[47]:

df2=df2.groupby([df2["Y"].dt.month]).count()


# In[48]:

li2=['BOROUGH']


# In[49]:

df2=df2[li2].sum(axis=1)


# In[60]:

df=df.to_frame().merge(df2.to_frame(), left_index=True, right_index=True)


# In[62]:

print(df)


# In[63]:

df['Result'] = df['0_x']/df['0_y']


# In[74]:

df.head()


# In[66]:

df.columns=("Manhattan","NewYork","Percentage")


# In[85]:

with open('Q1A1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Month','Manhattan','NewYork','Percentage'])


# In[87]:

with open('Q1A1.csv', 'a') as f:
    df.to_csv(f, header=False)


# In[ ]:



