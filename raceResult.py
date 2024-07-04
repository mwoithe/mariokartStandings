from init import Init
import exceptions as e

class Result:
    pointsAllocation = [None,15,12,10,9,8,7,6,5,4,3,2,1]
    def __init__(self, string, trackName, raceID):
        data = string.split(",")
        if len(data) != 2:
            raise e.DataReadError("Whoever did the checks should be sacked. This should not have got to here")
        
        if data[0] in Init.playerList:
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