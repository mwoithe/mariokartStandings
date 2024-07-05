from player import Player

class Team:
    def __init__(self, teamName, form=-1):
        self.name = teamName
        self.fileName = "data/teams/"+teamName+".txt"
        self.form = form
        self.members = self.getTeamMembers()
        self.points = self.calcTeamScore()
        self.wins = self.calcTeamWins()
        self.podiums = self.calcTeamPodiums()
        self.spoons = self.calcTeamSpoons()
        
    
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
    
    def calcTeamScore(self):
        points = 0
        for name in self.members:
            p = Player(name, self.form)
            points += p.points
        
        return points
    
    def calcTeamWins(self):
        wins = 0
        for name in self.members:
            p = Player(name, self.form)
            wins += p.wins
        
        return wins
    
    def calcTeamPodiums(self):
        podiums = 0
        for name in self.members:
            p = Player(name, self.form)
            podiums += p.podiums
        
        return podiums
    
    def calcTeamSpoons(self):
        spoons = 0
        for name in self.members:
            p = Player(name, self.form)
            spoons += p.spoons
        
        return spoons
    