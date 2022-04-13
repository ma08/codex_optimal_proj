import sys
import math

def main():
    n = int(sys.stdin.readline())
    s = float(sys.stdin.readline())
    holes = {}
    while n > 0:
        line = sys.stdin.readline()
        r, x, y, z = map(float, line.split())
        holes[(x, y, z)] = r
        n -= 1
    #print holes
    for x in range(0, int(s) + 1, 1):
        for y in range(0, int(s) + 1, 1):
            for z in range(0, int(s) + 1, 1):
                if x == 0 and y == 0 and z == 0:
                    continue
                if (x, y, z) in holes:
                    continue
                if math.sqrt(x**2 + y**2 + z**2) <= s:
                    print x, y, z


if __name__ == "__main__":
    main()
