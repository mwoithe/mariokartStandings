from player import Player

class Team:
    def __init__(self, teamName):
        self.name = teamName
        self.fileName = "data/teams/"+teamName+".txt"
        self.members = self.getTeamMembers()
        self.points = self.calculateTeamScore()
        # self.cumulativeTime = self.calculateTeamTime()
    
    def __lt__(self, other):
        return self.points < other.points
        
    def __gt__(self, other):
        return self.points > other.points
        
    def __eq__(self, other):
        return self.points == other.points
    

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
    
    def calculateTeamScore(self):
        points = 0
        for name in self.getTeamMembers():
            p = Player(name)
            points += p.calcPlayerScore()
        
        return points

    # def calculateTeamTime(self):
    #     time = Time(0,0,0)
    #     for name in self.getTeamMembers():
    #         p = Player(name)
    #         time += p.calcPlayerTime()
        
    #     return time
        





###################################################################################################

    # This may be surplus to requirements
    def getPlayerData(self, playerName):
        # check that player is in this team
        found = False
        for name in self.getTeamMembers():
            if name == playerName:
                found = True
                break
        
        if found:
            # create new player instance with playerName
            p = Player(playerName)

            # call player's getData method
            return p.getPlayerData()
        # 

    # in hindsight, this is probably unnecessary
    def addPlayer(self, playerName):
        i = input(f"Are you sure you want to add player {playerName} to team {self.name}? ")
        if i == "yes":
            f = open("Tournament/data/teams/"+self.name+".txt", "r")
            if f.read().__contains__("member="+playerName):
                input("Operation cancelled. Player may already exist in that team. \nplease check and try again")
            else:
                f = open("Tournament/data/teams/"+self.name+".txt", "a")
                f.write("\nmember="+playerName)
                print("player added")
            f.close()
        else:
            input("Operation cancelled")
        
    
        





        



# t1 = Team("team Fred", 19, Time(1,3,9))
# t2 = Team("team Daniel", 19, Time(1,9,1))
# t = Team("t")
# print(t.calculateTeamScore(), t.calculateTeamTime())

# print(t1 > t2)