
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame


# In[5]:


url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2013-14-legislative-session.html'


# In[6]:


result = requests.get(url)


# In[7]:


c = result.content


# In[5]:


c


# In[8]:


soup = BeautifulSoup(c, 'lxml')


# In[9]:


summary = soup.find('div', {'class':'list-land', 'id':'content'})
summary


# In[10]:


tables = summary.find_all('table')


# In[9]:


len(tables)


# In[11]:


data = []
rows = tables[0].find_all('tr')


# In[12]:


len(rows)


# In[20]:


for tr in rows:
    cols = tr.find_all('td')
    for td in cols:
        text = td.find(text=True)
        print(text)
        data.append(text)


# In[21]:


data


# In[22]:


reports = []
date = []
index = 0
for item in data:
    if 'pdf' in item:
        date.append(data[index-1])
        reports.append(item.replace('\xa0',' '))
    index += 1


# In[23]:


date


# In[24]:


date = Series(date)


# In[25]:


reports = Series(reports)


# In[26]:


web_df = pd.concat([date,reports], axis=1)


# In[27]:


web_df


# In[28]:


web_df.columns=['Date','Reports']


# In[29]:


web_df


# In[12]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'ファイル名.ipynb'])

