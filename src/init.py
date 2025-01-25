from player import Player
from team import Team

"""
What were doing here is:
- creating x number of players
- On creation, each player needs a data file.
   - each line in the data file is the player's result from a race
- each player is added to a team

"""
class Init:
    def __init__(self):
        f = open("data/races/usedIDs.txt", "w")
        f.close()
        # self.initPlayers()
        # self.initTeams()

        # reset other files
        f = open("data/resultInput.txt", "w")
        f.write("# DO NOT REMOVE FIRST 4 LINES\ntrackName=\nraceID=1\nplayer,placing\n")
        f.close()


    def initPlayers(self):
        opening = "name,raceID,track,placing,points"

        for playerName in Player.playerList:
            # create new file
            f = open("data/players/"+playerName+".csv", "w")
            f.write(opening)
            f.close()

    def initTeams(self):
        for teamName in Team.teamList:
            # create new file
            f = open("data/teams/"+teamName+".txt", "w")
            f.write("name="+teamName+"\n")
            f.close()
