import sys

class Point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

def main():
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        c = sys.stdin.readline().strip()
        points.append(Point(x, y, c))
    points.sort()
    for p in points:
        print(p.x, p.y, p.c)

if __name__ == '__main__':
    main()
