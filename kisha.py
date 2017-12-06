class Triangle:
    R = 0
    xC = 0
    yC = 0

    def __init__(self, x, y, R):
        g = bool(False)
        if R < 0:
            R = R * -1

        self.R = R
        self.xC = x
        self. yC = y
misha = Triangle(3, 3, -5)
print(misha.R)


