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
        try:
            checkFile = open("mariokartStandings/init/init.txt", "r")
            print("Warning: Initialisation has already been completed, doing so again will reset the whole thing. Procede with EXTREME CATUTION")
            checkFile.close()
            print("Reloading...")
            self.reload()
            return
        except FileNotFoundError as e:
            print("Starting init")

        # set up check file so this doesn't get done again
        f = open("mariokartStandings/init/init.txt", "w")
        f.write("Foobar")
        f.close()

        f = open("mariokartStandings/data/races/usedIDs.txt", "w")
        f.close()
        self.initPlayers()
        self.initTeams()

        # reset other files
        f = open("mariokartStandings/data/resultInput.txt", "w")
        f.write("# DO NOT REMOVE FIRST 4 LINES\ntrackName=\nraceID=1\nplayer,placing\n")
        for name in Player.playerList:
            f.write(f"{name},\n")
        f.close()


    def initPlayers(self):
        opening = "name,raceID,track,placing,points"

        for playerName in Player.playerList:
            # create new file
            f = open("mariokartStandings/data/players/"+playerName+".csv", "w")
            f.write(opening)
            f.close()

            # create new player
            Player(playerName)


    def initTeams(self):
        for teamName in Team.teamList:
            # create new file
            f = open("mariokartStandings/data/teams/"+teamName+".txt", "w")
            f.write("name="+teamName+"\n")
            f.close()

            # create new team
            Team(teamName)

    def reload(self):
        """This one is for when the program is reopened, but initilisation is not to be done again"""
        for playerName in Player.playerList:
            if Player.getPlayerByName(playerName) == None:
                Player(playerName)
        
        for teamName in Team.teamList:
            if Team.getTeamByName(teamName) == None:
                Team(teamName)
