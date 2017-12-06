class Nation:
    def getx(self):
        return self.__color * 3

    def setx(self):
        self.__color = int(self.__color)

    def delx(self):
        del self.__color

    color = property(getx, setx, delx)



kazax = Nation
kazax.color = "black"
print(kazax.color)
kazax.color
