
# coding: utf-8

# In[32]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv


# In[33]:

df=pd.read_csv('vehicle_collisions.csv')


# In[34]:

df=df.groupby([df["BOROUGH"]]).count()


# In[35]:

new = df.filter(['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'], axis=1)


# In[36]:

new['Sum']=new['VEHICLE 4 TYPE']+new['VEHICLE 5 TYPE']


# In[37]:

print(new)


# In[41]:

new=new.drop('VEHICLE 4 TYPE',axis=1)


# In[43]:

new=new.drop('VEHICLE 5 TYPE',axis=1)


# In[44]:

new.head()


# In[45]:

with open('Q1A2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Borough','One Vehicle Involved','Two Vehicle Involved','Three Vehicle Involved','Four or More Vehicles Involved'])


# In[46]:

with open('Q1A2.csv', 'a') as f:
    new.to_csv(f, header=False)
    


# In[ ]:



