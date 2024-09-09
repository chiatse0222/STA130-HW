#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# In[2]:


missing_values = df[df.isna().any(axis=1)]
print(missing_values)


# In[3]:


total_missing = df.isna().sum().sum()
print(total_missing)


# In[4]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Get a concise summary of the DataFrame
df.info()

# Get descriptive statistics for numerical columns
print(df.describe())

# Get descriptive statistics for all columns
print(df.describe(include='all'))


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.isna().sum()
df.describe()


# In[8]:


df.columns


# In[9]:


https://copilot.microsoft.com/sl/b35WCONNCr6


# In[1]:


print ('Observations refer to what each row represents in the dataset.')
print ('Variables refer to what each column represents in the dataset. ')
print ('In this context, observations provide information about each individual villager, while the variables represent specific characteristics, such as ID, name, gender, etc., one at a time.')


# In[2]:


print('An attribute is a feature of an object that stores information about it. We can access an attribute without using parentheses. For example, df.shape is an attribute that gives the number of rows and columns in the data.')
print('A method is a function linked to an object that performs actions on it. Methods usually require parentheses to be used. For example, df.describe() is a method that calculates and returns summary statistics for a dataset.')


# In[ ]:




