from mtime import Time
# from player import Player
from init import Init
import exceptions as e

class Result:
    def __init__(self, string):
        data = string.split(",")
        if len(data) != 2:
            raise e.DataReadError("Whoever did the checks should be sacked. This should not have got to here")
        
        if data[0] in Init.playerList:
            self.name = data[0]
        else:
            raise e.DataReadError("Whoever did the checks should be sacked. This should not have got to here")
        
        self.time = Time.readTime(data[1])

    def __lt__(self, other):
        return self.time < other.time
    
    def __gt__(self, other):
        return self.time > other.time
    
    def __eq__(self, other):
        return self.time == other.time