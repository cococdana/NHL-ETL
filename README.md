# Coco Dana Sportradar ETL Coding Challenge


## Completed code to build the pipeline is located in the file titled "playerStats.ipynb" and "teamStats.ipynb"

teamStats.ipynb contains code that returns a csv file when you provide a team id and season year. The csv includes stats and information about the provided team. 
  * Team ID
  * Team Name
  * Team Venue Name
  * Games Played
  * Wins
  * Losses
  * Points
  * Goals Per Game
  * Game Date of First Game of Season (includes pre-season)
  * Opponent Name in First Game of Season


playerStats.ipynb returns players information based on an input of a player id and season year. 
  * Player ID
  * Player Name
  * Current Team
  * Player Age
  * Player Number
  * Player Position
  * If the player is a rookie
  * Assists
  * Goals
  * Games
  * Hits
  * Points

Outcome csvs are titled "playerInfo.csv" and "teamInfo.csv." Each time the two programs in the notebook file are called, the csvs will update. 

The code to call the two pipelines are at the bottom of the notebook file. I also included Python versions of the two notebooks.

To test the pipelines, I called the two pipelines with the below inputs: 

getStatsForPerson('8476792', '20172018')

getStatsForYear('2', '20172018') 

which created the playerInfo.csv file and the teamInfo.csv file which are populated in this repo.

To test, I cross referenced my outcomes with Wikipedia stats and called the pipelines in the testing.ipnyb file.


## Details

All code was written in Jupyter notebooks.
To run locally, you must have pandas, numpy, and requests installed.

