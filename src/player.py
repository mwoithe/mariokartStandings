from exceptions import NoDataError
import team
from display import Display
from name import Name

def get_players():
    f = open("mariokartStandings/init/players.txt", "r")
    names = f.read().split("\n")
    f.close()
    return names

class Player:
    playerList = get_players()
    players = []

    def __init__(self, name, form=-1):
        Display.set_num_players(len(Player.playerList))

        if name not in Player.playerList:
            print(f"WARNING: `{name}` is not a registered player.")
            return
        
        for player in Player.players:
            if player.name == name:
                print(f"Player `{name}` already exists")
                player.refresh(form)
                return

        self.name = Name(name)
        self.fileName = f"mariokartStandings/data/players/{name}.csv"
        self.form = form
        self.colour = team.Team.getPlayerColour(name)
        self.data = self.getPlayerData()
        self.points = self.calcPlayerScore()
        self.wins = self.calcPlayerWins()
        self.podiums = self.calcPlayerPodiums()
        self.spoons = self.calcPlayerSpoons()

        Player.players.append(self)

        # print(name, "colour = ", self.colour)
        print(f"Registered player {name}. Number of registered players = {len(Player.players)}")

    def refresh(self, form):
        # print(f"Refreshing `{self.name}`")
        self.form = form
        self.colour = team.Team.getPlayerColour(self.name.get_name())
        self.data = self.getPlayerData()
        self.points = self.calcPlayerScore()
        # print(f"self.points = {self.points}")
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
        if other == None:
            return False
        else:
            return (self.points == other.points and
                self.wins == other.wins and
                self.podiums == other.podiums and
                self.spoons == other.spoons)
    
    def logRaceResult(self, result):
        # "name,raceID,track,placing,points"
        log = f"\n{self.name.get_current()},{result.raceID},{result.track},{result.placing},{result.points}"
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
        
        try:
            if len(data)-1 < self.form:
                raise NoDataError(f"Number of races requested ({self.form}) exceeds available race data ({len(data)-1})")
            elif len(data) == 1:
                raise NoDataError(f"Player '{self.name.get_name()}' has no race data availabe")
            return data
        except NoDataError as e:
            print(e.message)
            return []
    
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
            if row[3] == str(len(Player.players)):
                spoons += 1
        return spoons
    
    def calcPlayerScoreAlt(self):
        pointsAllocation = [None,21,17,14,11,9,7,5,4,3,2,1,0]
        data = self.data[(-self.form):]
        score = 0
        for row in data:
            score += pointsAllocation[int(row[3])]
        return score

    def getPlayerBar(self, pos):
        ## TODO Using get_name(), may want get_current(). Not sure at this point
        return f"""<div class="player-row {self.colour}">
            <div class="col-1 row-col">
                {pos}
            </div>
            <div class="col-3 row-col">
                {self.name.get_name()} 
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
    # Returns a match if name given matches either name or current alias
    def getPlayerByName(cls, name):
        for player in cls.players:
            if player.name.get_name() == name or player.name.get_current() == name:
                return player
        
        return None
    
    def __str__(self):
        return f"Player `{self.name.get_name()}` (currently known as `{self.name.get_current()}`): {self.points} points, {self.wins} wins, {self.podiums} podiums and {self.spoons} spoons."
    
    def changeName(self, newname):
        for p in Player.players:
            if p.name.get_name() == newname or p.name.get_current() == newname:
                print(f"ERROR: could not change `{self.name.get_name()}`'s name. Alias `{newname}` already in use")
                return

        self.name.set_current(newname)
