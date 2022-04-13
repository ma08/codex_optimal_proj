import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pair:
    def __init__(self, r, b):
        self.r = r
        self.b = b

def main():
    n = int(sys.stdin.readline())
    r_list = []
    b_list = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        r_list.append(Point(x, y))
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        b_list.append(Point(x, y))
    pairs = []
    for i in range(n):
        for j in range(n):
            if r_list[i].x < b_list[j].x and r_list[i].y < b_list[j].y:
                pairs.append(Pair(r_list[i], b_list[j]))
    print(len(pairs))

if __name__ == '__main__':
    main()
