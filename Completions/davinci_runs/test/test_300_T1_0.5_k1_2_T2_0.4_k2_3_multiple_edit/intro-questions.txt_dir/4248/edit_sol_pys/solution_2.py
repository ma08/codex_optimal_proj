import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __repr__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def distance(self, other):
        """Returns the distance between this point and another point."""
        dist_x = self.x - other.x
        dist_y = self.y - other.y
        return math.sqrt(dist_x ** 2 + dist_y ** 2)

    def angle(self, other):
        """Returns the angle (in radians) of the line between this point and another point."""
        dist_x = other.x - self.x
        dist_y = other.y - self.y
        return math.atan2(dist_y, dist_x)

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
        self.slope = (point2.y - point1.y) / (point2.x - point1.x)
        self.y_int = point1.y - self.slope * point1.x

    def __str__(self):
        return "%s -> %s" % (self.p1, self.p2)

    def __repr__(self):
        return "%s -> %s" % (self.p1, self.p2)

    def __eq__(self, other):
        return self.slope == other.slope and self.y_int == other.y_int

    def __ne__(self, other):
        return not self.__eq__(other)

    def distance(self, point):
        """Returns the distance between the given point and the line."""
        return abs(self.slope * point.x - point.y + self.y_int) / math.sqrt(self.slope ** 2 + 1)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Center: %s, Radius: %f" % (self.center, self.radius)

    def __repr__(self):
        return "Center: %s, Radius: %f" % (self.center, self.radius)

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_inside(self, point):
        """Returns True if the given point is inside the circle, False otherwise."""
        return self.center.distance(point) < self.radius

    def is_outside(self, point):
        """Returns True if the given point is outside the circle, False otherwise."""
        return self.center.distance(point) > self.radius

    def is_on(self, point):
        """Returns True if the given point is on the circle, False otherwise."""
        return self.center.distance(point) == self.radius

    def is_inside_or_on(self, point):
        """Returns True if the given point is inside or on the circle, False otherwise."""
        return self.center.distance(point) <= self.radius

    def is_outside_or_on(self, point):
        """Returns True if the given point is outside or on the circle, False otherwise."""
        return self.center.distance(point) >= self.radius

    def point_distance(self, point):
        """Returns the distance between the given point and the circle."""
        return self.center.distance(point) - self.radius

    def line_distance(self, line):
        """Returns the distance between the given line and the circle."""
        return line.distance(self.center) - self.radius

    def intersection(self, line):
        """Returns the intersection points between the given line and the circle."""
        if line.distance(self.center) > self.radius:
            return []
        elif line.distance(self.center) == self.radius:
            return [self.center]
        else:
            dist_x = self.center.x - line.p1.x
            dist_y = self.center.y - line.p1.y
            d = math.sqrt(dist_x ** 2 + dist_y ** 2)
            if d == 0:
                return [line.p1]
            else:
                a = math.acos((self.radius ** 2 + d ** 2 - line.distance(self.center) ** 2) / (2 * d * self.radius))
                b = math.atan2(dist_y, dist_x)
                return [Point(self.center.x + self.radius * math.cos(b - a), self.center.y + self.radius * math.sin(b - a)),
                        Point(self.center.x + self.radius * math.cos(b + a), self.center.y + self.radius * math.sin(b + a))]

class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.s1 = self.p1.distance(self.p2)
        self.s2 = self.p2.distance(self.p3)
        self.s3 = self.p3.distance(self.p1)
        self.a = self.p1.angle(self.p2)
        self.b = self.p2.angle(self.p3)
        self.c = self.p3.angle(self.p1)
        self.area = 0.5 * self.s1 * self.s2 * math.sin(self.c)

    def __str__(self):
        return "%s, %s, %s" % (self.p1, self.p2, self.p3)

    def __repr__(self):
        return "%s, %s, %s" % (self.p1, self.p2, self.p3)

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_inside(self, point):
        """Returns True if the given point is inside the triangle, False otherwise."""
        t1 = Triangle(self.p1, self.p2, point)
        t2 = Triangle(self.p2, self.p3, point)
        t3 = Triangle(self.p3, self.p1, point)
        return t1.area + t2.area + t3.area < self.area

    def is_outside(self, point):
        """Returns True if the given point is outside the triangle, False otherwise."""
        return not self.is_inside(point)

    def is_on(self, point):
        """Returns True if the given point is on the triangle, False otherwise."""
        return self.p1.distance(point) + self.p2.distance(point) + self.p3.distance(point) == self.s1 + self.s2 + self.s3

    def is_inside_or_on(self, point):
        """Returns True if the given point is inside or on the triangle, False otherwise."""
        return self.is_inside(point) or self.is_on(point)

    def is_outside_or_on(self, point):
        """Returns True if the given point is outside or on the triangle, False otherwise."""
        return not self.is_inside(point) or self.is_on(point)

    def point_distance(self, point):
        """Returns the distance between the given point and the triangle."""
        if self.is_on(point):
            return 0
        elif self.is_inside(point):
            return -1
        else:
            d1 = Line(self.p1, self.p2).distance(point)
            d2 = Line(self.p2, self.p3).distance(point)
            d3 = Line(self.p3, self.p1).distance(point)
            return min(d1, d2, d3)

    def line_distance(self, line):
        """Returns the distance between the given line and the triangle."""
        if self.is_inside_or_on(line.p1) and self.is_inside_or_on(line.p2):
            return -1
        else:
            d1 = line.distance(self.p1)
            d2 = line.distance(self.p2)
            d3 = line.distance(self.p3)
            return min(d1, d2, d3)

    def circle_distance(self, circle):
        """Returns the distance between the given circle and the triangle."""
        if self.is_inside_or_on(circle.center):
            return -1
        else:
            d1 = circle.line_distance(Line(self.p1, self.p2))
            d2 = circle.line_distance(Line(self.p2, self.p3))
            d3 = circle.line_distance(Line(self.p3, self.p1))
            return min(d1, d2, d3)

def read_points(n):
    """Reads n points from the input, returns a list of the points."""
    points = []
    for i in range(n):
        x, y = [float(x) for x in input().split()]
        points.append(Point(x, y))
    return points

def main():
    n = int(input())
    points = read_points(n)
    points.sort(key=lambda p: p.x)
    triangle = Triangle(points[0], points[1], points[2])
    while triangle.is_inside(points[3]):
        triangle = Triangle(points[1], points[2], points[3])
    while triangle.is_outside(points[3]):
        triangle = Triangle(points[0], points[1], points[2])
    for i in range(4, n):
        if triangle.is_inside(points[i]):
            while triangle.is_inside(points[i]):
                triangle = Triangle(points[1], points[2], points[i])
        elif triangle.is_outside(points[i]):
            while triangle.is_outside(points[i]):
                triangle = Triangle(points[0], points[1], points[2])
    print(triangle.circle_distance(Circle(triangle.p1, triangle.s1)))

if __name__ == '__main__':
    main()
