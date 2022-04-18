import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    y = int(sys.stdin.readline().strip())
    x = int(sys.stdin.readline().strip())
    rods = []
    for i in range(n-1):
        rods.append(math.sqrt((int(sys.stdin.readline().strip())-x)**2 + (int(sys.stdin.readline().strip())-y)**2))
    rods.sort()
    while len(rods) > 1:
        rods[0] += rods.pop(-1)
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
