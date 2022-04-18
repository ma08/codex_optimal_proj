import sys
import math

def is_inside(x, y, x1, y1, x2, y2, x3, y3):
    area1 = abs(x*(y2-y3) + x2*(y3-y) + x3*(y-y2))/2
    area2 = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
    area3 = abs(x1*(y-y3) + x*(y3-y1) + x3*(y1-y))/2
    area4 = abs(x1*(y2-y) + x2*(y-y1) + x*(y1-y2))/2
    if (area1 + area2 + area3 + area4) == abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)):
        return True
    return False

def main():
    x1, y1 = map(int, sys.stdin.readline().rstrip().split())
    x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    x3, y3 = map(int, sys.stdin.readline().rstrip().split())
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        if is_inside(x, y, x1, y1, x2, y2, x3, y3):
            count += 1
    print(abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)
    print(count)

main()
