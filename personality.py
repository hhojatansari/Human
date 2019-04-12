class Personality():

    def __init__(self):
        self.__first_name = "ND_FNAME"
        self.__last_name = "ND_LNAME"
        self.__nationality = "ND_NATIONALITY"

    def set_name(self, fname, lname):
        self.__first_name = fname
        self.__last_name = lname

    def get_name(self):
        return self.__first_name, self.__last_name

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def get_nationality(self):
        return self.__nationality
