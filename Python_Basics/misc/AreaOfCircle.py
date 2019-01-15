import math

class CircleArea:
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = CircleArea(4)
print(p.area())
print(p.circle_area(4))