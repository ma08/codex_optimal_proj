# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

class Points(object):
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.w = w
        self.z = z

    def __sub__(self, other):
        return Points(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def cross(self, other):
        return Points(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(5):
        a = list(map(float, input().split()))

        points.append(a)

    a, b, c, d, e = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3]), Points(*points[4])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c).cross(e - d)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
