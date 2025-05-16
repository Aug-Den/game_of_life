class Cell():

    __CONSTANTE_GRID_INITAL =" 🥚"

    def __init__(self, coordinate):
        __coordinate = coordinate

    # coordinate getter funct
    @property
    def coordinate(self):
        return self.__coordinate
    
    # coordinate setter funct
    @coordinate.setter 
    def coordinate(self, coordinate): 
        self.__coordinate = coordinate