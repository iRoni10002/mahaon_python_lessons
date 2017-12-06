class Triangle:

    def get(self):
        return self.__color * 3

    def set(self):
        self.__color = int(self.__color)

    R = property(get, set)
    y = property(get, set)
    x = property(get, set)

misha = Triangle
misha.R = 5
misha.x = 3
misha.y = 6


