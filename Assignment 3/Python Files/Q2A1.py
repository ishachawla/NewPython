
# coding: utf-8

# In[33]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv


# In[34]:

df=pd.read_csv('employee_compensation.csv')


# In[35]:

df=df.groupby(["Organization Group","Department"])[['Total Compensation']].mean()


# In[36]:

df=df.sort(['Total Compensation'], ascending=[0])


# In[37]:

df.head()


# In[ ]:




# In[ ]:




# In[39]:

with open('Q2A1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Organization','Department','Total Compensation'])


# In[40]:

with open('Q2A1.csv', 'a') as f:
    df.to_csv(f, header=False)


# In[ ]:



