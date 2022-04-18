import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def absolute(self): #norm
        return math.sqrt(self.x * self.x + self.y * self.y)


if __name__ == '__main__':
    a = Point(*map(int, input().split()))
    b = Point(*map(int, input().split()))
    c = Point(*map(int, input().split()))
    d = Point(*map(int, input().split()))

    x = (b - a).cross(c - b) 
    y = (c - b).cross(d - c) 
    angle = math.degrees(math.acos(x * y / ((b - a).absolute() * (c - b).absolute())))

    print("%.2f" % angle)
