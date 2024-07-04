"""
What were doing here is:
- creating x number of players
- On creation, each player needs a data file.
   - each line in the data file is the player's result from a race
- each player is added to a team

"""

class Init:
    playerList = [
        "Emule",
        "Wilbur",
        "Gnu",
        "Amanda",
        "Nolok",
        "Puffy"
        # "freddy" #etc
    ]
    numPlayers = len(playerList)
    
    teamList = [
        "red",
        "blue"
    ]

    def __init__(self):
        # self.players = []
        # self.teams = []
        pass

    def initPlayers(self, names):
        opening = "name,raceID,track,placing,points"

        for playerName in names:
            # create new file
            f = open("data/players/"+playerName+".csv", "w")
            f.write(opening)
            f.close()

    def initTeams(self, teams):
        for teamName in teams:
            # create new file
            f = open("data/teams/"+teamName+".txt", "w")
            f.write("name="+teamName+"\n")
            f.close()


            



# I = Init()
# I.initPlayers(Init.playerList)
# I.initTeams(Init.teamList)