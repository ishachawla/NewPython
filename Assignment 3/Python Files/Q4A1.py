
# coding: utf-8

# In[220]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv
import re
import numpy as np


# In[221]:

df=pd.read_csv('movies_awards.csv')


# In[222]:

df1=df[['Title','Awards']]


# In[223]:

df1=df1.dropna()


# In[224]:


df1["Wins"] = df1["Awards"].apply(lambda x : (re.findall(r"(\d+) win", x)))
df1["Nominations"] = df1["Awards"].apply(lambda x : (re.findall(r"(\d+) nomination", x)))
df1["Golden Globes Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Golden", x)))
df1["Golden Globes Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Golden", x)))
df1["Oscars Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Oscar", x)))
df1["Oscars Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Oscar", x)))
df1["Bafta Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) BAFTA", x)))
df1["Bafta Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) BAFTA", x)))
df1["PrimeTime Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Primetime", x)))
df1["PrimeTime Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Primetime", x)))
df1.head()

# In[225]:

with open('Q4A1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title','Awards','Wins','Nominations','Golden Globes Won','Golden Globes Nominated','Oscars Nominated','Oscars Won','Bafta Nominated','Bafta Won','Primetime Won','Primetime Nominated'])


# In[226]:

with open('Q4A1.csv', 'a') as f:
    df1.to_csv(f, header=False)


# In[ ]:




# In[ ]:




# In[ ]:



