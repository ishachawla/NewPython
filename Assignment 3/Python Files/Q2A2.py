
# coding: utf-8

# In[19]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv


# In[41]:

df=pd.read_csv('employee_compensation.csv')


# In[42]:

df=df.groupby(["Employee Identifier","Job Family"])[['Salaries','Overtime','Total Benefits','Total Compensation']].mean()


# In[43]:

df=df.query('Overtime>0.05*Salaries')


# In[ ]:




# In[44]:

df['Percentage']=(df['Total Benefits']/df['Total Compensation'])*100


# In[45]:

df.head(10)


# In[46]:

df=df.sort(['Percentage'], ascending=[0])


# In[48]:

with open('Q2A2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Employee','JobFamily','Total Benefits','Total Compensation','Percentage'])


# In[49]:

df=df.drop('Salaries',axis=1)
df=df.drop('Overtime',axis=1)


# In[50]:

with open('Q2A2.csv', 'a') as f:
    df.to_csv(f, header=False)


# In[ ]:



