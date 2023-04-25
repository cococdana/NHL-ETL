#!/usr/bin/env python
# coding: utf-8

# In[149]:


import pandas as pd
import numpy as np
import requests
from pandas.core.frame import DataFrame
import json
import json
import csv


# In[150]:


def getStatsForPerson(person,year):
    
    ENDPOINT = "https://statsapi.web.nhl.com/api/v1/people/"
    
    # make a request to the endpoint
    response = requests.get(f"{ENDPOINT}{person}") 
    #second request for player stats
    response2 = requests.get(f"{ENDPOINT}{person}" +"/stats/?stats=statsSingleSeason&season="+ f"{year}")
    
    if response.status_code == 200 & response2.status_code ==200: #make sure calls to APIs worked
        
        data = response.json()
        
        name = data['people'][0]['fullName']
        playerNum = data['people'][0]['currentTeam']['id']
        playerTeam = data['people'][0]['currentTeam']['name']
        age = data['people'][0]['currentAge'] 
        pos = data['people'][0]['primaryPosition']['name']
        rookie = data['people'][0]['rookie']
        
        data2 = response2.json()
        
        assists = data2['stats'][0]['splits'][0]['stat']["assists"]
        goals = data2['stats'][0]['splits'][0]['stat']["goals"]
        hits = data2['stats'][0]['splits'][0]['stat']["hits"]
        games = data2['stats'][0]['splits'][0]['stat']["games"]
        points= data2['stats'][0]['splits'][0]['stat']["points"]
        
        #format csv output 
        playerID = "Player ID: "+ f'{person}'
        name = "Player Name: "+ f'{name}'
        playerTeam = "Current Team: "+ f'{playerTeam}'
        age = "Player Age: "+ f'{age}'
        playerNum = "Player Number: "+ f'{playerNum}'
        pos = "Player Position: "+ f'{pos}'
        rookie = "Rookie?: " +f'{rookie}'
        assists = "Assists: "+ f'{assists}'
        goals = "Goals: "+ f'{goals}'
        hits = "Hits: "+ f'{hits}'
        games = "Games: "+ f'{games}'
        points = "Points: "+ f'{points}'
      
        # Save info in an array
        nparray = np.array([playerID,name,playerTeam,age,playerNum,pos,rookie,assists,goals,hits,games,points],dtype=str)      
        np.savetxt("playerInfo.csv", nparray,fmt='%s', delimiter=",")
        print("outcome file titled <playerInfo.csv> created.")

    else:
        raise Exception(response.text)

print("Notebook playerStats has been run. Choose a team ID and season to be inputted in the pipeline. For example run {getStatsForPerson('8476792', '20172018')}")


# In[151]:


#getStatsForPerson('8476792', '20172018')


# In[ ]:




