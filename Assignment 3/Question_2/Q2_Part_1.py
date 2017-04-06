
# coding: utf-8

# # EMPLOYEE COMPENSATION ANALYSIS
# ## Q2_PART ONE
# 
# - Use 'employee_compensation' data set.
# 
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# 
# - Output should contain the organization group and the departments in each organization group with the total compensationfrom highest to lowest value.
# 
# - Display a few rows of the outputuse df.head().
# 
# - Generate a csv output.

# In[13]:

# importing all the packages needed 
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[15]:

path = os.getcwd() # getting the current working directory
configfile = os.path.join(os.getcwd() + '\\Data\\employee_compensation.csv') # getting the path of the json files to be read


# In[6]:

# filtering the specific columns needed alone
fields = ['Organization Group', 'Department', 'Total Compensation']
df = pd.read_csv(configfile,skipinitialspace=True, usecols=fields)


# In[7]:

Total_Compensation_Group = df.groupby(['Organization Group', 'Department']).mean() # calculating the mean of the groupped data


# In[14]:

# groupping the data with level 0 and sorting them in decending order
Total_Compensation_Group_Sort = Total_Compensation_Group['Total Compensation'].groupby(level=0, group_keys=False)
Employee_Compensation = pd.DataFrame(Total_Compensation_Group_Sort.apply(lambda x: x.order(ascending=False)).reset_index())
print(Employee_Compensation.head()) # displaying the first 5 records


# In[10]:

# exporting the analysed data to a csv file
Employee_Compensation.to_csv(os.path.join(path + '\Outputs\Q2_Part_1\Q2_Part_1.csv'),index=True)

