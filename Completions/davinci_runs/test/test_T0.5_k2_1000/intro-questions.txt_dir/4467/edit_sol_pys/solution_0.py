import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pair:
    def __init__(self, red, blue):
        self.red = red
        self.blue = blue

def main():
    n = int(sys.stdin.readline())
    red = []
    blue = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        red.append(Point(x, y))
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        blue.append(Point(x, y))
    pairs = []
    for i in range(n):
        for j in range(n):
            if red[i].x < blue[j].x and red[i].y < blue[j].y:
                pairs.append(Pair(red[i], blue[j]))
    print(len(pairs))

if __name__ == '__main__':
    main()
