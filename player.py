class Player:
    def __init__(self, name):
        self.name = name
        self.fileName = "data/players/"+name+".csv"
        self.points = self.calcPlayerScore()
    
    def __lt__(self, other):
        return self.points < other.points
        
    def __gt__(self, other):
        return self.points > other.points
        
    def __eq__(self, other):
        return self.points == other.points
    

    def getPlayerData(self):
        """Returns a list of all rows of player data."""
        f = open(self.fileName, "r")
        lines = f.read().split("\n")
        f.close()
        
        data = []
        for line in lines:
            data.append(line.split(","))
            
        # print( data)
        return data
    
    def calcPlayerScore(self):
        data = self.getPlayerData()[1:]
        score = 0
        for row in data:
            score += int(row[4])
        return score
    
    def logRaceResult(self, result):
        # "name,raceID,track,placing,points"
        log = f"\n{self.name},{result.raceID},{result.track},{result.placing},{result.points}"
        f = open(self.fileName, "a")
        f.write(log)
        f.close()

# p = Player("Wilbur")

# print(p.calcPlayerScore())
# print(p.calcPlayerTime())