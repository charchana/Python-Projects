
# coding: utf-8

# # EMPLOYEE COMPENSATION ANALYSIS
# ## Q2_PART TWO
# - Use 'employee_compensation' data set.
# 
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# 
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# 
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value. 
# 
# - Displaythe top 5 Job Families according to this percentage value usingdf.head().
# 
# - Write the output (jobs and percentage value) to a csv.

# In[1]:

# importing all the packages needed 
import os
import pandas as pd


# In[2]:

path = os.getcwd() # getting the path of current working directory to create the folder structure
configfile = os.path.join(path + '\Data' + '\\employee_compensation.csv') # getting the path of the json files to be read


# In[3]:

df = pd.read_csv(configfile) # READING THE CSV FILE
Calendar_Data = df[df['Year Type'] == 'Calendar'] # filtering the calendar data


# In[4]:

# filtering the specific columns
Calendar_Data_Details = Calendar_Data[["Salaries","Overtime","Other Salaries","Total Salary","Retirement","Health/Dental","Other Benefits","Total Benefits","Total Compensation"]]


# In[5]:

# groupping the data with employee id and calculating the mean
Employees_Group = Calendar_Data.groupby(['Employee Identifier'])["Salaries","Overtime","Other Salaries","Total Salary","Retirement","Health/Dental","Other Benefits","Total Benefits","Total Compensation"].mean().reset_index()
Employees_Group_Frame = pd.DataFrame(Employees_Group)


# In[6]:

# filtering the data with overtime > salaries 5 %
fivePercentCheck = Employees_Group_Frame[Employees_Group_Frame.Overtime > (0.05*Employees_Group_Frame.Salaries)]


# In[7]:

# grouping the data with job family and employee id
jobFamily = Calendar_Data[['Employee Identifier','Job Family']]
jobFamily = jobFamily.drop_duplicates()


# In[8]:

mergedFrame = pd.merge(jobFamily,fivePercentCheck, on = 'Employee Identifier' ) # merging the two frames


# In[9]:

# grouping the data frame with job family and calculating the mean
Employees_Group = mergedFrame.groupby(['Job Family'])['Total Benefits','Total Compensation'].mean().reset_index()
Employees_Group_Frame = pd.DataFrame(Employees_Group)


# In[10]:

# assigning the percentage value to a new column
Employees_Group_Frame['Percent Total Benefit'] = (Employees_Group_Frame['Total Benefits']/Employees_Group_Frame['Total Compensation'])*100


# In[11]:

# sorting the data with percent value in decending order
Employees_Group_Frame = Employees_Group_Frame.sort_values('Percent Total Benefit', ascending = 0)
print(Employees_Group_Frame.head())


# In[12]:

# exporting the analysed data to a csv file 
Employees_Group_Frame.to_csv(os.path.join(path + '\Outputs\Q2_Part_2\Q2_Part_2.csv'),index=False)

