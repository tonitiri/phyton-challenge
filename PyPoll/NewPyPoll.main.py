#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%% Dependencies
import pandas as pd
import numpy as np


# In[2]:


# Save path to data set in a variable
data_file = "C:\\Users\\taiwo\\OneDrive\\Desktop\\phyton-challenge\\PyPoll\\Resources\\election_data.csv"


# In[12]:


# The total number of votes
count = data_file_pd["Voter ID"].count()
count


# In[4]:


# Display a statistical overview of the DataFrame
data_file_pd.describe()


# In[5]:


# List of candidates & total number of votes won
count = data_file_pd["Candidate"].value_counts()
count


# In[11]:


# List of candidates & percentage of votes won
count = data_file_pd["Candidate"].value_counts(max)
count


# In[30]:


# Winner
count = data_file_pd["Candidate"].value_counts()
count.head(1)


# In[32]:





# In[31]:





# In[ ]:




