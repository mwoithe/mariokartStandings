

class Name:
    def __init__(self, name):
        self.__name = name
        self.__current = name

    def get_name(self):
        return self.__name
    
    def get_current(self):
        return self.__current
    
    def set_current(self, new):
        self.__current = new