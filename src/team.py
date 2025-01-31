# from player import Player
import player as p
from display import Display

class Team:
    teamList = [
        "Milk",
        "Maximus",
        "Nut Bars",
        "Naver"
    ]

    teams = []

    def __init__(self, teamName, form=-1):
        Display.set_num_teams(len(Team.teamList))
        self.name = teamName
        self.fileName = "mariokartStandings/data/teams/"+teamName+".txt"
        self.form = form
        self.members = self.getTeamMembers()
        self.colour = self.getTeamColour()
        self.points = self.calcTeamScore()
        self.wins = self.calcTeamWins()
        self.podiums = self.calcTeamPodiums()
        self.spoons = self.calcTeamSpoons()

        Team.teams.append(self)
        print("List of teams:", Team.teams)
        
    
    def __lt__(self, other):
        if self.points < other.points:
            return True
        elif self.points == other.points:
            # if points are equal, rank on wins
            if self.wins < other.wins:
                return True
            elif self.wins == other.wins:
                # If wins are equal, rank on podium finishes 
                if self.podiums < other.podiums:
                    return True
                elif self.podiums == other.podiums:
                    # If it gets to here, the team with the most last places is lower
                    return self.spoons > other.spoons
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __gt__(self, other):
        if self.points > other.points:
            return True
        elif self.points == other.points:
            # if points are equal, rank on wins
            if self.wins > other.wins:
                return True
            elif self.wins == other.wins:
                # If wins are equal, rank on podium finishes 
                if self.podiums > other.podiums:
                    return True
                elif self.podiums == other.podiums:
                    # If it gets to here, the team with the least last places is higher
                    return self.spoons < other.spoons
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __eq__(self, other):
        return (self.points == other.points and
                self.wins == other.wins and
                self.podiums == other.podiums and
                self.spoons == other.spoons)
    
    def showTeamReport(self):
        pass
    
    def getTeamMembers(self):
        """
        Extracts the team's members from the team data file, and returns them as a String array
        """
        f = open(self.fileName, "r")
        data = f.read().split("\n")
        f.close()
        
        members = []
        for line in data:
            if line[0:7] == "member=":
                members.append(line[7:])
        
        return members
    
    def getTeamColour(self):
        """
        Extracts the team's colour from the team data file, and returns it as a string
        """
        f = open(self.fileName, "r")
        data = f.read().split("\n")
        f.close()
        
        colour = ""
        for line in data:
            if line[0:7] == "colour=":
                colour = line[7:]
                break

        print(colour)
        return colour
    
    def calcTeamScore(self):
        points = 0
        for name in self.members:
            player = p.Player(name, self.form)
            points += player.points
        
        return points
    
    def calcTeamWins(self):
        wins = 0
        for name in self.members:
            player = p.Player(name, self.form)
            wins += player.wins
        
        return wins
    
    def calcTeamPodiums(self):
        podiums = 0
        for name in self.members:
            player = p.Player(name, self.form)
            podiums += player.podiums
        
        return podiums
    
    def calcTeamSpoons(self):
        spoons = 0
        for name in self.members:
            player = p.Player(name, self.form)
            spoons += player.spoons
        
        return spoons
    
    def getTeamBar(self, pos):
        return f"""     <div class="team-row {self.colour}">
            <div class="col-1 row-col">
                {pos}
            </div>
            <div class="col-3 row-col">
                {self.name}
            </div>
            <div class="col-2 row-col">
                {self.points}
            </div>
            <div class="col-2 row-col">
                {self.wins}
            </div>
            <div class="col-2 row-col">
                {self.podiums}
            </div>
            <div class="col-2 row-col">
                {self.spoons}
            </div>
        </div>"""
    
    @classmethod
    def getPlayerColour(cls, player):
        for team in Team.teams:
            for name in team.members:
                if name == player:
                    return team.colour
