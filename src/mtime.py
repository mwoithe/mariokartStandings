import exceptions as e
import re

class Time:
    def __init__(self, minutes, seconds=0, msecs=0):
        if not (0 <= msecs <= 999):
            raise e.InvalidTimeException("msecs must be between 0 and 999")
        if not (0 <= seconds <= 59):
            raise e.InvalidTimeException("seconds must be between 0 and 59")
        if not (0 <= minutes):
            raise e.InvalidTimeException("minutes must be greater than 0")
        
        self.min : int = minutes
        self.sec : int = seconds
        self.msecs : int = msecs

    def __add__(self, other):
        min = self.min + other.min
        sec = self.sec + other.sec
        msec = self.msecs + other.msecs

        if msec >= 1000:
            msec -= 1000
            sec += 1

        if sec >= 60:
            sec -= 60
            min += 1

        return Time(min, sec, msec)
    
    def __sub__(self, other):
        min = self.min - other.min

        if min < 0:
            raise e.NegativeTimeException()
        else:
            sec = self.sec - other.sec
            if sec < 0:
                min -= 1
                sec = 60 + sec
            
            msec = self.msecs - other.msecs
            if msec < 0:
                sec -= 1
                msec = 1000 + msec
                if sec < 0:
                    min -= 1
                    sec = 60 + sec
            
            if min < 0:
                raise e.NegativeTimeException()
            else:
                return Time(min, sec, msec)

    def __int__(self):
        return self.min * 60 * 1000 + self.sec * 1000 + self.msecs

    def __lt__(self, other):
        return int(self) < int(other)
    
    def __gt__(self, other):
        return int(self) > int(other)
    
    def __eq__(self, other):
        return int(self) == int(other)

    def __str__(self):
        time = ""

        if 0 <= self.msecs < 10:
            time = ".00" + str(self.msecs)
        elif 10 <= self.msecs < 100:
            time = ".0" + str(self.msecs)
        elif 100 <= self.msecs < 1000:
            time = "." + str(self.msecs)
        else:
            pass # I don't think we should get here
        
        if 0 <= self.sec < 10:
            time = ":0" + str(self.sec) + time
        elif 10 <= self.sec < 60:
            time = ":" + str(self.sec) + time
        else:
            pass # I don't think we should get here

        if self.min >= 0:
            return f"{self.min}" + time
        else:
            pass # I don't think we should get here

    @staticmethod
    def readTime(time):
        """
        Takes a time as a string, and returns a Time if the string is sound.
        """
        pattern = "^[0-9]+:[0-5][0-9][.][0-9][0-9][0-9]$"
        match = re.findall(pattern, time)
        if match.__len__() != 1:
            raise e.InvalidTimeException("Time format is incorrect")

        nums = match[0].split(":")
        nums = [nums[0], nums[1].split(".")[0], nums[1].split(".")[1]]
        for i in [0,1,2]:
            nums[i] = int(nums[i])

        return Time(nums[0], nums[1], nums[2])





# time1 = Time(1, 59, 12)
# time2 = Time(1, 0, 122)
# print(str(time1) + "\n" + str(time2))
# print(str(time1 > time2))
# print(Time.readTime("0:23.093"))
