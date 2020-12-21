

class minicad():
    def __init__(self,_name):
        self.__name = _name
        self.__color = "black"
        self.__thickness = 3

    @property
    def color(self):
        return self.__color
    def thickness(self):
        return self.__thickness

    @color.setter
    def color(self,_color):
        self.__color = _color
    def thickness(self,_thickness):
        self.__thickness = _thickness

class Dot(minicad):
    def __init__(self, _posX, _posY,):
        self.__X = _posX
        self.__Y = _posY

    @property
    def X(self):
        return self.__X
    def Y(self):
        return self.__Y

