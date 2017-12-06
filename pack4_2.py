class Point:

    count = 0
    coord_x = int()
    coord_y = int()

    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y
        Point.count += 1

    def __add__(self, point):
        x = self.coord_x + point.coord_x
        y = self.coord_y + point.coord_y
        return [x, y]

    @staticmethod
    def get_count(self):
        return Point.count

    @classmethod
    def get_class(cls):
        return cls(Point, point1)

point1 = Point(2, 6)
point2 = Point(1, 2)
point3 = Point(point1.__add__(point2)[0], point1.__add__(point2)[1])
print(point3.coord_x, point3.coord_y)
print(Point.get_count(Point))
print(Point.get_class())
