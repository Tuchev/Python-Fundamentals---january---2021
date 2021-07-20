class Shape:
    def get_area(self):
        return None


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def get_area(self):
        return 0.5 * self.side * self.h


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * 2


shapes = [Triangle(3, 6), Triangle(5, 8), Square(3), Square(10)]

for shape in shapes:
    print(shape.get_area())
