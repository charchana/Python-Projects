
# coding: utf-8

# # MOVIE AWARDS ANALYSIS
# ## Q4_PART ONE
# 
# - Use ‘movies_awards’ data set.
# 
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# 
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# 
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
# 
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
# 
# - Create two separate columns for each award category (won and nominated).
# 
# - Write your output to a csv file. (Sample output is given in next page)
# 

# In[1]:

# importing all the packages needed 
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:

path = os.getcwd() # getting the path of current working directory to create the folder structure
configfile = os.path.join(path + '\Data' + '\\movies_awards.csv') # getting the path of the json files to be read


# In[3]:

# filtering the specific columns needed alone and dropping the NAN rows
fields = ["Awards","Title"]
AWARDS = pd.read_csv(configfile,skipinitialspace=True, usecols=fields)
AWARDS = AWARDS.dropna(axis=0)


# In[4]:

# Extracting the values for awards won columns based on the string patterns needed for each particluar column
AWARDS["Awards_Won"]=AWARDS["Awards"].str.extract('(\d+) win').fillna(0).astype(int)
AWARDS["Golden Globe_Awards_Won"]=AWARDS["Awards"].str.extract('Won (\d+) Golden Globe').fillna(0).astype(int)
AWARDS["Oscar_Awards_Won"]=AWARDS["Awards"].str.extract('Won (\d+) Oscar').fillna(0).astype(int)
AWARDS["Primetime_Awards_Won"]=AWARDS["Awards"].str.extract('Won (\d+) Primetime').fillna(0).astype(int)
AWARDS["BAFTA Film_Awards_Won"]=AWARDS["Awards"].str.extract('Won (\d+) BAFTA Film').fillna(0).astype(int)


# In[5]:

# Extracting the values for awards nominated columns based on the string patterns needed for each particluar column
AWARDS["Awards_Nominated"]=AWARDS["Awards"].str.extract('(\d+) nomination').fillna(0).astype(int)
AWARDS["Oscar_Awards_Nominated"]=AWARDS["Awards"].str.extract('Nominated for (\d+) Oscar').fillna(0).astype(int)
AWARDS["Golden_Globe_Awards_Nominated"]=AWARDS["Awards"].str.extract('Nominated for (\d+) Golden Globe').fillna(0).astype(int)
AWARDS["Primetime_Awards_Nominated"]=AWARDS["Awards"].str.extract('Nominated for (\d+) Primetime').fillna(0).astype(int)
AWARDS["BAFTA Film_Awards_Nominated"]=AWARDS["Awards"].str.extract('Nominated for (\d+) BAFTA Film').fillna(0).astype(int)


# In[6]:

# adding all the columns needed to find the total awards won and nominated
AWARDS["Total_Awards_Won"]= AWARDS.ix[:,'Awards_Won':'BAFTA Film_Awards_Won'].sum(axis=1)
AWARDS["Total_Awards_Nominated"]= AWARDS.ix[:,'Awards_Nominated':'BAFTA Film_Awards_Nominated'].sum(axis=1)


# In[18]:

# Rearranging the column names as how to be displayed
MOVIE_AWARDS = AWARDS[['Title','Awards','Awards_Won','Awards_Nominated', 'Oscar_Awards_Nominated', 'Golden_Globe_Awards_Nominated', 'Primetime_Awards_Nominated', 
                 'BAFTA Film_Awards_Nominated','Oscar_Awards_Won', 'Golden Globe_Awards_Won', 'Primetime_Awards_Won', 'BAFTA Film_Awards_Won', 'Total_Awards_Won', 'Total_Awards_Nominated' ]] #+ [AWARDS[8]] + cols[3:6] + cols[8:12] + [cols[-7]] + [cols[-1]]
print (MOVIE_AWARDS.head(5))


# In[9]:

# exporting the analysed data to a csv file 
MOVIE_AWARDS.to_csv(os.path.join(path + '\Outputs\Q4_Part_1.csv'),index=False)


# In[ ]:



