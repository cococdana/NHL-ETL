#!/usr/bin/env python
# coding: utf-8

# In[135]:


import pandas as pd
import numpy as np
import requests
from pandas.core.frame import DataFrame
import json
import json
import csv


# In[144]:


def getStatsForYear(team, year):
    
    teamEndPoint = "https://statsapi.web.nhl.com/api/v1/teams/"
    scheduleEndPoint = "https://statsapi.web.nhl.com/api/v1/schedule/"
    
    # make a request to the endpoint
    venueInfo = requests.get(f"{teamEndPoint}{team}")
    teams = requests.get(f"{scheduleEndPoint}"+"?teamId="+f"{team}"+"&season=" + f"{year}")
    response = requests.get(f"{teamEndPoint}{team}"+"/stats" +"?season=" + f"{year}") # making a request to the correct endpoint
   
    if response.status_code == 200 & venueInfo.status_code ==200 & teams.status_code == 200: #make sure calls to APIs worked
        
        data = response.json() #seasoninfo
        data2 = venueInfo.json() #venueinfo
        data3 = teams.json() #teamStats
        
        splits = data['stats'][0]['splits'][0]["stat"]
        gamesPlayed = splits['gamesPlayed']
        wins = splits['wins']
        losses = splits['losses']
        points= splits['pts']
        goalsPerGame= splits['goalsPerGame']
                             
        venue = data2['teams'][0]['venue']['name']
        
        firstGame = data3['dates'][0]['date']
        team1 = data3['dates'][0]['games'][0]['teams']['away']['team']['name']
        team1ID = data3['dates'][0]['games'][0]['teams']['away']['team']['id']
        team2 = data3['dates'][0]['games'][0]['teams']['home']['team']['name']
        team1ID = data3['dates'][0]['games'][0]['teams']['away']['team']['id']
        
        #format csv output 
        venue = "Team Venue: "+f'{venue}'
        gamesPlayed="Games Played: " +f'{gamesPlayed}'
        wins= "Wins: " +f'{wins}'
        losses="Losses: "+f'{losses}'
        points="Points: "+f'{points}'
        goalsPerGame="Goals Per Game: "+f'{goalsPerGame}'
        firstGame="Date of first game: " +f'{firstGame}'
        if team1ID == team: #get team name and opponent name
            oppo="Opponent Name: "+f'{team2}'
            teamName = team1
        else: 
            oppo="Opponent Name: "+f'{team1}'
            teamName = team2
        
        teamID = "Team ID: "+f'{team}'
        teamName = "Team Name: "+f'{teamName}'
 
        # Save info in an array
        nparray = np.array([teamID,teamName,venue,gamesPlayed,wins,losses,points,goalsPerGame,firstGame,oppo],dtype=str)
        np.savetxt("teamInfo.csv", nparray,fmt='%s', delimiter=",")    
       

    else:
        raise Exception(response.text)



getStatsForYear('2', '20172018')


# In[145]:


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


    else:
        raise Exception(response.text)


getStatsForPerson('8476792', '20172018')


# In[ ]:




