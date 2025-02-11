# from player import Player
import player as p
from display import Display

def get_teams():
    f = open("mariokartStandings/init/teams.txt", "r")
    names = f.read().split("\n")
    f.close()
    return names

class Team:
    teamList = get_teams()

    teams = []

    def __init__(self, teamName, form=-1, colour=""):
        Display.set_num_teams(len(Team.teamList))

        if teamName not in Team.teamList:
            print(f"<WARNING> `{teamName}` is not a registered team.")
            return
        
        for team in Team.teams:
            # If the team already exists, refresh it
            if team.name == teamName:
                print(f"<INFO> Refreshing team {teamName}.")
                team.refresh(colour=colour)
                return

        self.name = teamName
        self.fileName = f"mariokartStandings/data/teams/{teamName}.txt"

        # self.form = form
        self.colour = self.getTeamColour()
        self.members = self.getTeamMembers()

        self.points = self.calcTeamScore()
        self.wins = self.calcTeamWins()
        self.podiums = self.calcTeamPodiums()
        self.spoons = self.calcTeamSpoons()

        Team.teams.append(self)
        # print(f"{teamName} = {self.colour}")
        print(f"<INFO> Registered team {teamName}. Number of registered teams = {len(Team.teams)}")
        
    def refresh(self, colour=""):
        if colour != "":
            self.changeTeamColour(colour)
        
        self.colour = self.getTeamColour()
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
        if type(other) != type(self) or other is None:
            return False
        else:
            return (self.points == other.points and
                self.wins == other.wins and
                self.podiums == other.podiums and
                self.spoons == other.spoons)
    
    def getTeamMembers(self):
        """
        Extracts the team's members from the team data file, and returns them as a Player array
        """
        f = open(self.fileName, "r")
        data = f.read().split("\n")
        f.close()
        
        members = []
        for line in data:
            if line[0:7] == "member=":
                name = line[7:]
                player = p.Player.getPlayerByName(name)
                members.append(player)
        
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

        # print(colour)
        return colour
    
    def changeTeamColour(self, new_colour):
        colour_list = [
            "blue",
            "green",
            "grey",
            "lime",
            "orange",
            "pink",
            "purple",
            "red",
            "sky",
            "yellow",
            "dark-grey",
            "black",
            "white",
            "maroon"
        ]

        if new_colour not in colour_list:
            print("<WARNING> Colour was not changed - colour not valid")
            return

        f = open(self.fileName, "r")
        data = f.read().split("\n")
        f.close()

        f = open(self.fileName, "w")
        success = False

        for line in data:
            if line[0:7] == "colour=":
                f.write("colour=" + new_colour + "\n")
                success = True
            else:
                f.write(line + "\n")
        
        if not success:
            f.write("colour=" + new_colour + "\n")
            success = True

        f.close()
        print(f"<INFO> Team `{self.name}`'s colour successfully changed to {new_colour}")
        return
    
    def calcTeamScore(self):
        points = 0
        for person in self.members:
            points += person.points
        
        return points
    
    def calcTeamWins(self):
        wins = 0
        for person in self.members:
            wins += person.wins
        
        return wins
    
    def calcTeamPodiums(self):
        podiums = 0
        for person in self.members:
            podiums += person.podiums
        
        return podiums
    
    def calcTeamSpoons(self):
        spoons = 0
        for person in self.members:
            spoons += person.spoons
        
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
    def getPlayerColour(cls, player_name):
        for team in Team.teams:
            for player in team.members:
                if player.name.get_name() == player_name or player.name.get_current() == player_name:
                    return team.colour

    @classmethod
    def getTeamByName(cls, name):
        for team in cls.teams:
            if team.name == name:
                return team
        return None
    
    def addPlayer(self, player_name):
        if player_name not in p.Player.playerList:
            print(f"<WARNING> Player `{player_name}` could not be assigned  - `{player_name}` is not a registered player")
            return
        
        # Check if player is in another team
        found_in = None
        for team in Team.teams:
            for player in team.members:
                if player.name.get_name() == player_name and team.name == self.name:
                    print(f"<INFO> Player `{player_name}` is already in team `{self.name}`.")
                    return
                elif player.name.get_name() == player_name:
                    found_in = team
                    print(f"<INFO> Player `{player_name}` is already in team `{team.name}`")
                    if input(f"\n<INPUT REQUEST> Do you wish to remove them from {team.name} and add to `{self.name}`? [Type 'yes' to proceed]\n+ ") != "yes":
                        return
                    # break

        # Remove from current team
        if found_in != None:
            found_in.removePlayer(player_name)

        # add to this one
        f = open(self.fileName, "a")
        f.write(f"member={player_name}\n")
        f.close()


        print(f"<INFO> Player `{player_name}` successfully added to team `{self.name}`.")
        self.members = self.getTeamMembers()
        return

    def removePlayer(self, player_name):
        player = p.Player.getPlayerByName(player_name)
        if player not in self.members:
            print(f"<WARNING> Couldn't remove player `{player.name.get_name()}` from team `{self.name}` - `{player.name.get_name()}` is not in team `{self.name}`")
            return
        
        f = open(self.fileName, "r")
        data = f.read().split("\n")
        f.close()

        f = open(self.fileName, "w")
        success = False

        for line in data:
            if line[0:7] == "member=" and line[7:] == player.name.get_name():
                success = True
            else:
                f.write(line + "\n")

        f.close()
        print(f"<INFO> Player `{player.name.get_name()}` successfully removed from team `{self.name}`")
        self.members = self.getTeamMembers()
        return