class SalleCinema:
    def __init__(self, nom, place):
        self.__nom = nom
        self.__place = place

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value