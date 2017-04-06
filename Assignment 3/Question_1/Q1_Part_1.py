
# coding: utf-8

# # NYC VEHICLE COLLISION ANALYSIS
# ## Q1_PART ONE
# 
# - Use ‘vehicle_collisions’ data set.
# 
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# 
# - Display a few rows of the outputuse df.head().
# 
# - Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)
# 

# In[1]:

# importing all the packages needed 
import os
import pandas as pd
import calendar


# In[2]:

path = os.getcwd() # getting the path of current working directory to create the folder structure
configfile = os.path.join(path + '\Data' + '\\vehicle_collisions.csv') # getting the path of the json files to be read


# In[3]:

# filtering the specific columns needed alone and filling the NAN rows as 0
fields = ['DATE', 'BOROUGH']
df = pd.read_csv(configfile,skipinitialspace=True, usecols=fields)
df = df.fillna(0)


# In[4]:

# extracting year and month from the date field as seperate YEAR ans MONTH column
df['DATE'] = pd.to_datetime(df['DATE'])
df['YEAR'], df['MONTH'] = df['DATE'].apply(lambda x: x.year), df['DATE'].apply(lambda x: x.month)


# In[5]:

year2016 = df[(df['YEAR'] == 2016)] # filtering the year 2016 data
year2016 = year2016.sort_values(['MONTH'], ascending=1) # sorting the data with month
year2016['MONTH'] = year2016['MONTH'].apply(lambda x: calendar.month_abbr[x]) # changing the month format


# In[6]:

months = year2016.groupby(['MONTH'], sort = False).size().to_frame().reset_index() # grouping by month and finding the count
cond = (year2016['BOROUGH'] == 'MANHATTAN') # filtering manhattan data
manMonth = year2016[cond].groupby(['MONTH'], sort = False).size().to_frame().reset_index() # grouping by month for manhattand data and finding count
manMonth.rename(columns = {0:'MANHATTAN'}, inplace=True) # renaming the columns
months.rename(columns = {0:'NYC'}, inplace=True) # renaming the columns


# In[7]:

manhattanNYC = manMonth.merge(months, how = 'outer') # merging the dataframes
percent = manhattanNYC['MANHATTAN']/manhattanNYC['NYC'] # finding the percentage of collisions
manhattanNYC['PERCENTAGE'] = percent # creating a new cloumn for percent
manhattanNYC.rename(columns = {2: 'NYC', 1:'MANHATTAN'}, inplace=True) # renaming the columns 
print(manhattanNYC.head())


# In[8]:

# exporting the analysed data to a csv file 
manhattanNYC.to_csv(os.path.join(path + '\Outputs\Q1_Part_1\Q1_Part_1.csv'),index=False)


# In[ ]:



