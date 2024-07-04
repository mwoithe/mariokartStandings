from player import Player
from init import Init
from raceResult import Result
import re
import exceptions as e

class Race:
    dataFile = "data/resultInput.txt"

    def __init__(self):
        if self.checkData():
            self.track = None
            self.id = None
            if self.readData():
                input("Data logging complete")
        else:
            input("Insertion cancelled [press enter to exit]")
    
    def checkData(self):
        print("\n----------------------------------------\n",
              "Checking race data:")
        
        f = open("data/resultInput.txt", "r")
        
        file = f.read()
        f.close()
        t = file.split("player,placing\n")
        
        # deal with the key: values
        info = t[0]

        # check for a trackName
        track = re.findall("trackName=.+", info)
        if len(track) != 1:
            if len(track) == 0:
                raise e.DataInputError(Race.dataFile, "No trackName found")
            else:
                raise e.DataInputError(Race.dataFile, "More than one 'trackName' field was found")
        else:
            track = track[0][10:]

        print("Track Name OK")

        # check for a raceID
        id = re.findall("raceID=[0-9]+", info)
        if len(id) != 1:
            if len(id) == 0:
                raise e.DataInputError(Race.dataFile, "No raceID number found. If field exists, please check the value is a number")
            else:
                raise e.DataInputError(Race.dataFile, "More than one 'raceID' field was found")
        else:
            id = int(id[0][7:])

        print("Race ID OK")

        # Deal with the player times
        raceData = t[1]
        times = raceData.split("\n")

        entry = 1
        for time in times:
            test = time.split(",")
            
            if len(test) != 2:
                raise e.DataInputError(Race.dataFile, f"Something's wrong with data entry #{entry}: incorrect number of values")
            else:
                if test[0] == "" or test[1] == "":
                    raise e.DataInputError(Race.dataFile, f"Something's wrong with data entry #{entry}: At least one entry is empty")
                else:
                    if test[0] not in Init.playerList:
                        raise e.DataInputError(Race.dataFile, f"Something's wrong with data entry #{entry}: {test[0]} is not a listed player")
                    
                    try:
                        place = int(test[1])
                        if not 1 <= place <= len(Init.playerList):
                            raise ValueError
                    except ValueError:
                        raise e.DataInputError(Race.dataFile, f"Something's wrong with data entry #{entry}: '{test[1]}' is not a valid placing")
                    # int(test[1])
                    
                    print(f"Data entry #{entry} OK")
            
            entry += 1

        if input("\n\nData check complete. \nDo you wish to log this result? " +
              "\nWARNING: Faulty data is very hard to undo, and may cause catastrophic issues. " +
              "\nOnly proceed if ALL tests have passed, and you are sure no errors are present. " +
              "\nThe previous checks DO NOT GUARANTEE no errors are present" +
              "\n\nDo you wish to proceed? [Type 'yes' to proceed, any other input cancels]\n") == "yes":
            return True
        else:
            return False

        # print(times)

    def readData(self):
        f = open(Race.dataFile, "r")
        file = f.read()
        f.close()
        t = file.split("player,placing\n")
        
        # deal with the key: values
        info = t[0]

        # check for a trackName
        track = re.findall("trackName=.+", info)
        self.track = track[0][10:]

        # check for a raceID
        id = re.findall("raceID=[0-9]+", info)
        self.id = int(id[0][7:])

        # Deal with the player placings
        raceData = t[1]
        placings = raceData.split("\n")
        res = []
        for place in placings:
            res.append(Result(place, self.track, self.id))
        
        res.sort(reverse=True)
        f = open("data/races/" + str(self.id) + self.track + ".csv", "w")
        f.write("player,placing,points")

        for result in res:
            f.write(f"\n{result.name},{result.placing},{result.points}")
            p = Player(result.name)
            p.logRaceResult(result)
        
        f.close()

        return True

        



r = Race()
