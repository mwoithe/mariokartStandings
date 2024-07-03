from mtime import Time

class Player:
    def __init__(self, name):
        self.name = name
        self.fileName = "Tournament/data/players/"+name+".csv"
        self.points = self.calcPlayerScore()
        self.cumulativeTime = self.calcPlayerTime()
    
    def __lt__(self, other):
        if self.points < other.points:
            return True
        elif self.points == other.points:
            # If level on points, the player with the least time is higher
            return self.cumulativeTime > other.cumulativeTime
        else:
            return False
        
    def __gt__(self, other):
        if self.points > other.points:
            return True
        elif self.points == other.points:
            # If level on points, the player with the least time is higher
            return self.cumulativeTime < other.cumulativeTime
        else:
            return False
        
    def __eq__(self, other):
        return (self.points == other.points) and (self.cumulativeTime == other.cumulativeTime)
    

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
            score += int(row[5])
        # self.score = score
        return score
    
    def calcPlayerTime(self):
        data = self.getPlayerData()[1:]
        time = Time(0,0,0)
        for row in data:
            time += Time.readTime(row[3])
        # self.cumulativeTime = time
        return time

# p = Player("Wilbur")

# print(p.calcPlayerScore())
# print(p.calcPlayerTime())