#!/usr/bin/env python
# coding: utf-8

# In[12]:


#%% Dependencies
import pandas as pd
import numpy as np


# In[2]:


# Save path to data set in a variable
data_file = "C:\\Users\\taiwo\\OneDrive\\Desktop\\phyton-challenge\\PyBank\\Resources\\budget_data.csv"


# In[21]:


# Use Pandas to read data
data_file_pd = pd.read_csv(data_file)
data_file_pd.head


# In[30]:


# Display a statistical overview of the DataFrame


# In[31]:


# Reference a single column within a DataFrame


# In[32]:


# The mean method averages the series


# In[9]:


# The net total amount of "Profit/Losses" over the entire period
total = data_file_pd["Profit/Losses"].sum()
total


# In[14]:


# The total number of months
count = data_file_pd["Date"].count()
count


# In[24]:


# Calculations of changes in Profit/Losses
changes_in_Profit_Losses = data_file_pd['Profit/Losses'].diff()
data_file_pd["changes_in_Profit_Losses"] = changes_in_Profit_Losses

data_file_pd.head()


# In[25]:


# The average of the changes in "Profit/Losses" over the entire period
average = data_file_pd["changes_in_Profit_Losses"].mean()
average


# In[36]:


# The greatest increase in profits (date and amount) over the entire period
count = data_file_pd["changes_in_Profit_Losses"].max()
count


# In[37]:


# The greatest decrease in losses (date and amount) over the entire period
count = data_file_pd["changes_in_Profit_Losses"].min()
count


# In[ ]:




