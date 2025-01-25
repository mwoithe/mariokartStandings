from team import Team
from player import Player
# import time

class Standings:
    def __init__(self):
        pass

    def displayTeamStandings(self, form=-1):
        teams = []
        for name in Team.teamList:
            teams.append(Team(name, form))
        
        teams.sort(reverse=True)
        message = "\tTeam\tPoints\tWins\tPodiums\tSpoons\n"
        pos = 1
        for team in teams:
            message += f"{pos}\t{team.name}\t{team.points}\t{team.wins}\t{team.podiums}\t{team.spoons}\n"
            pos += 1
        
        print(message)
        f = open("data/standings.txt", "w")
        f.write(message)
        f.close()


    def displayIndStandings(self, form=-1):
        # Store the player instances, because these can be compared easily 
        players = []
        for name in Player.playerList:
            players.append(Player(name, form))

        players.sort(reverse=True)
        message = "\tPlayer\tPoints\tWins\tPodiums\tSpoons\n"
        pos = 1
        for player in players:
            message += f"{pos}\t{player.name}\t{player.points}\t{player.wins}\t{player.podiums}\t{player.spoons}\n"
            pos += 1
        
        print(message)
        f = open("data/standings.txt", "w")
        f.write(message)
        f.close()
        
s=Standings()
# s.displayIndStandings()
s.displayTeamStandings()