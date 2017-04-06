
# coding: utf-8

# # CRICKET MATCHES ANALYSIS
# ## Q3_PART ONE
# 
# - Use ‘cricket_matches’ data set.
# 
# - Calculate the average score for each team which host the game and win the game.
# 
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# 
# - Display a few rows of the outputuse df.head()
# 
# - Generate a csv output
# 

# In[1]:

# Import all the necessary package 
import pandas as pd
import os 


# In[28]:

# getting the path and reading the csv file
path = os.getcwd()
cricket_matches=pd.read_csv(path+"\\Data\\cricket_matches.csv")


# In[11]:

HOST_WINNER = pd.DataFrame(cricket_matches[cricket_matches['home'] == cricket_matches['winner']]) # finding the winner states


# In[8]:

HOST_INNINGS1 = pd.DataFrame(HOST_WINNER[HOST_WINNER['home'] == HOST_WINNER['innings1']]) #finding which innings the state played


# In[9]:

HOST_INNINGS2 = pd.DataFrame(HOST_WINNER[HOST_WINNER['home'] == HOST_WINNER['innings2']]) #finding which innings the state played


# In[18]:

HOST_INNINGS1_RUNS= HOST_INNINGS1[["home","innings1_runs"]].copy() # assigning the home and innings1 runs to frame
HOST_INNINGS1_RUNS.rename(columns={'home': 'HOME', 'innings1_runs': 'SCORE'}, inplace=True) # renaming the column names


# In[19]:

HOST_INNINGS2_RUNS= HOST_INNINGS2[["home","innings2_runs"]].copy() # assigning the home and innings2 runs to frame
HOST_INNINGS2_RUNS.rename(columns={'home': 'HOME', 'innings2_runs': 'SCORE'}, inplace=True) # renaming the column names


# In[21]:

INNINGS1_INNINGS2_RUNS =pd.concat([HOST_INNINGS1_RUNS, HOST_INNINGS2_RUNS], ignore_index=True) # joining both the innings frames 


# In[27]:

AVERAGE_SCORE = INNINGS1_INNINGS2_RUNS.groupby('HOME').mean().round(0).reset_index() # grouping by home and finding the average
print(AVERAGE_SCORE.head())


# In[29]:

# exporting the analysed data to a csv file 
AVERAGE_SCORE.to_csv(os.path.join(path + '\Outputs\Q3_Part_1.csv'),index=False )

