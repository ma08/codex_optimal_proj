
import sys
import math

def get_prob(r, x, y, z, s):
    if s < r:
        return 0.0
    if s == r:
        return 1.0
    if s > r:
        return 0.0

    return 0.0

def main():
    n = int(sys.stdin.readline())
    s = int(sys.stdin.readline())
    holes = []
    while n > 0:
        line = sys.stdin.readline()
        r, x, y, z = map(int, line.split())
        holes.append((r, x, y, z))
        n -= 1
    for i in range(0, n):
        r, x, y, z = holes[i]
        print get_prob(r, x, y, z, s)

if __name__ == "__main__":
    main()
