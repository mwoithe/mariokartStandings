from player import Player 
import exceptions as e

class Result:
    # pointsAllocation = [None,15,12,10,9,8,7,6,5,4,3,2,1]
    # pointsAllocation = [None,42,36,31,27,23,20,17,14,12,10,8,6,5,4,3,2,1,0]
    pointsAllocation = [None,21,17,14,11,9,7,5,4,3,2,1,0]
    def __init__(self, string, trackName, raceID):
        data = string.split(",")
        if len(data) != 2:
            raise e.DataReadError("Whoever did the checks should be sacked. This should not have got to here")
        
        if data[0] in Player.playerList:
            self.name = data[0]
        else:
            raise e.DataReadError("Whoever did the checks should be sacked. This should not have got to here")
        
        self.placing = int(data[1])
        self.points = Result.pointsAllocation[self.placing]
        self.track = trackName
        self.raceID = raceID

    def __lt__(self, other):
        return self.placing < other.placing
    
    def __gt__(self, other):
        return self.placing > other.placing
    
    def __eq__(self, other):
        return self.placing == other.placing