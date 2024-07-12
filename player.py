from init import Init
from exceptions import NoDataError

class Player:
    def __init__(self, name, form=-1):
        self.name = name
        self.fileName = "data/players/"+name+".csv"
        self.form = form
        self.data = self.getPlayerData()
        self.points = self.calcPlayerScore()
        self.wins = self.calcPlayerWins()
        self.podiums = self.calcPlayerPodiums()
        self.spoons = self.calcPlayerSpoons()
    
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
                    # If it gets to here, the player with the most last places is lower
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
                    # If it gets to here, the player with the least last places is higher
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
    
    def logRaceResult(self, result):
        # "name,raceID,track,placing,points"
        log = f"\n{self.name},{result.raceID},{result.track},{result.placing},{result.points}"
        f = open(self.fileName, "a")
        f.write(log)
        f.close()

    def getPlayerData(self):
        """Returns a list of all rows of player data: each row is its own list, with values as separated by commas in the file"""
        f = open(self.fileName, "r")
        lines = f.read().split("\n")
        f.close()
        
        data = []
        n = 0
        for line in lines:
            data.append(line.split(","))
            n+=1
        
        if len(data)-1 < self.form:
            raise NoDataError(f"Number of races requested ({self.form}) exceeds available race data ({len(data)-1})")
        elif len(data) == 1:
            raise NoDataError(f"Player '{self.name}' has no race data availabe")
        return data
    
    def calcPlayerScore(self):
        data = self.data[(-self.form):]
        score = 0
        for row in data:
            score += int(row[4])
        return score
    
    def calcPlayerWins(self):
        data = self.data[(-self.form):]
        wins = 0
        for row in data:
            if row[3] == "1":
                wins += 1
        return wins
    
    def calcPlayerPodiums(self):
        data = self.data[(-self.form):]
        podiums = 0
        for row in data:
            if row[3] in ["1", "2", "3"]:
                podiums += 1
        return podiums
    
    def calcPlayerSpoons(self):
        data = self.getPlayerData()[(-self.form):]
        spoons = 0
        for row in data:
            if row[3] == str(Init.numPlayers):
                spoons += 1
        return spoons
