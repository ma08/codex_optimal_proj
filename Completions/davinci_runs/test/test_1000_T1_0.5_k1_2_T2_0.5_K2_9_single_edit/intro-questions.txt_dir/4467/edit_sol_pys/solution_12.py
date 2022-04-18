
import sys

class Point:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.y < other.y:
            return True
        if self.y == other.y and self.x < other.x:
            return True
        return False

def main():
    n = int(sys.stdin.readline())
    reds = []
    blues = []
    for i in range(n):
        reds.append(Point(*map(int, sys.stdin.readline().split())))
    for i in range(n):
        blues.append(Point(*map(int, sys.stdin.readline().split())))
    reds.sort()
    blues.sort()
    count = 0
    for i in range(n):
        for j in range(n):
            if reds[i].x < blues[j].x and reds[i].y < blues[j].y:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()
