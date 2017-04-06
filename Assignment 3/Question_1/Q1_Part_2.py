
# coding: utf-8

# # NYCVEHICLE COLLISION ANALYSIS
# ## Q1_PART TWO
# 
# - Use ‘vehicle_collisions’ data set.
# 
# - For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# 
# - Display a few rows of the outputuse df.head().
# 
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')
# 

# In[1]:

# importing all the packages needed 
import os
import pandas as pd
import calendar
import numpy as np


# In[66]:

path = os.getcwd() # getting the path of current working directory to create the folder structure
configfile = os.path.join(path + '\Data' + '\\vehicle_collisions.csv') # getting the path of the json files to be read


# In[33]:

# filtering the specific columns needed alone and dropping the NAN rows
fields = ['DATE','BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE']
VEHICLE_COLLISION = pd.read_csv(configfile,skipinitialspace=True, usecols=fields)
VEHICLE_COLLISION = VEHICLE_COLLISION.dropna(subset=['BOROUGH'])


# In[35]:

# We are replacing the string value of vehicle type with 1 
VEHICLE_COLLISION['VEHICLE 1 TYPE'] = VEHICLE_COLLISION['VEHICLE 1 TYPE'].str.replace('.*', '1')
VEHICLE_COLLISION['VEHICLE 2 TYPE'] = VEHICLE_COLLISION['VEHICLE 2 TYPE'].str.replace('.*', '1')
VEHICLE_COLLISION['VEHICLE 3 TYPE'] = VEHICLE_COLLISION['VEHICLE 3 TYPE'].str.replace('.*', '1')
VEHICLE_COLLISION['VEHICLE 4 TYPE'] = VEHICLE_COLLISION['VEHICLE 4 TYPE'].str.replace('.*', '1')
VEHICLE_COLLISION['VEHICLE 5 TYPE'] = VEHICLE_COLLISION['VEHICLE 5 TYPE'].str.replace('.*', '1')


# In[36]:

VEHICLE_COLLISION = VEHICLE_COLLISION.fillna(0) # filling the nan values with 0


# In[40]:

# summing all the vehicle type values
VEHICLE_COLLISION["VEHICLE_COUNT"] = VEHICLE_COLLISION[['VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE']].astype(int).sum(axis=1)


# In[42]:

# assing the sum to a new column
VEHICLE_COLLISION["TOTAL_VEHICLE_COUNT"]= VEHICLE_COLLISION["VEHICLE_COUNT"]


# In[45]:

# summing the total count of each vehicle count value
VEHICLE_COLLISION_COUNT= pd.DataFrame(VEHICLE_COLLISION.groupby(["BOROUGH", 'VEHICLE_COUNT']).TOTAL_VEHICLE_COUNT.sum().reset_index())


# In[21]:

BOROUGH= VEHICLE_COLLISION_COUNT.BOROUGH.unique() # finding the unique borough values
VEHICLEs= VEHICLE_COLLISION_COUNT.VEHICLE_COUNT.unique() # finding the unique vehicle count values


# In[47]:

# looping through the dictionary to to find the number of vehicles for each borough
temp=[]
vehiclesCountList = []
for each in BOROUGH:
    for C1,C2,C3 in zip(VEHICLE_COLLISION_COUNT.BOROUGH, VEHICLE_COLLISION_COUNT.VEHICLE_COUNT, VEHICLE_COLLISION_COUNT.TOTAL_VEHICLE_COUNT): 
            if C1 == each:
                temp.append(C3)
    vehiclesCountList.append(temp)
    temp=[]   


# In[54]:

# creating the columns of the final analysis frame
VEHICLE_FRAME = pd.DataFrame(vehiclesCountList, columns=["ZERO_VEHICLE_INVOLVED","ONE_VEHICLE_INVOLVED","TWO_VEHICLE_INVOLVED","THREE_VEHICLE_INVOLVED","FOUR_VEHICLE_INVOLVED","FIVE_VEHICLE_INVOLVED"])


# In[55]:

VEHICLE_FRAME.drop(["ZERO_VEHICLE_INVOLVED"], axis=1, inplace=True) # dropping the list of 0 vehicle count


# In[56]:

VEHICLES_ANALYSIS = pd.DataFrame(BOROUGH,columns=["BOROUGH"]) # creating the borough data frame


# In[57]:

VEHICLES_ANALYSIS= pd.concat([VEHICLES_ANALYSIS, VEHICLE_FRAME], axis=1) # merging the borough with the vehicle count


# In[58]:

# calculating the sum for all the number of vehicles
VEHICLES_ANALYSIS["TWO_VEHICLE_INVOLVED"]= (VEHICLES_ANALYSIS["TWO_VEHICLE_INVOLVED"]/2).astype(int)
VEHICLES_ANALYSIS["THREE_VEHICLE_INVOLVED"]= (VEHICLES_ANALYSIS["THREE_VEHICLE_INVOLVED"]/3).astype(int)
VEHICLES_ANALYSIS["FOUR_VEHICLE_INVOLVED"]= (VEHICLES_ANALYSIS["FOUR_VEHICLE_INVOLVED"]/4).astype(int)
VEHICLES_ANALYSIS["FIVE_VEHICLE_INVOLVED"]= (VEHICLES_ANALYSIS["FIVE_VEHICLE_INVOLVED"]/5).astype(int)
VEHICLES_ANALYSIS["MORE_VEHICLE_INVOLVED"] = VEHICLES_ANALYSIS["FOUR_VEHICLE_INVOLVED"]+VEHICLES_ANALYSIS["FIVE_VEHICLE_INVOLVED"]
VEHICLES_ANALYSIS.drop(["FOUR_VEHICLE_INVOLVED","FIVE_VEHICLE_INVOLVED"], axis=1, inplace=True)


# In[60]:

# final frame data 
print(VEHICLES_ANALYSIS.head(3))


# In[65]:

# exporting the analysed data to a csv file 
VEHICLES_ANALYSIS.to_csv(os.path.join(path + '\Outputs\Q2_Part_2\Q2_Part_2.csv'),index=False)

