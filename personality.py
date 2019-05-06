class Personality():

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__nationality = "ND_NATIONALITY"

    def set_name(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_name(self):
        return self.__first_name, self.__last_name

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def get_nationality(self):
        return self.__nationality
