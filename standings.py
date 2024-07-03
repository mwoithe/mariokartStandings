from team import Team
from player import Player
from init import Init

class Standings:
    def __init__(self):
        pass

    def displayTeamStandings(self):
        teams = []
        for name in Init.teamList:
            teams.append(Team(name))
        
        teams.sort(reverse=True)
        message = "\tTeam\tPoints\tTime\n"
        pos = 1
        for team in teams:
            message += f"{pos}\t{team.name}\t{team.points}\t{team.cumulativeTime}\n"
            pos += 1
        
        print(message)
        f = open("Tournament/data/standings.txt", "w")
        f.write(message)
        f.close()


    def displayIndStandings(self):
        # Store the player instances, because these can be compared easily 
        players = []
        for name in Init.playerList:
            players.append(Player(name))

        players.sort(reverse=True)
        message = "\tPlayer\tPoints\tTime\n"
        pos = 1
        for player in players:
            message += f"{pos}\t{player.name}\t{player.points}\t{player.cumulativeTime}\n"
            pos += 1
        
        print(message)
        f = open("Tournament/data/standings.txt", "w")
        f.write(message)
        f.close()
        

s = Standings()
# s.displayIndStandings()
s.displayTeamStandings()