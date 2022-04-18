

import sys
import math

def main():
    line = sys.stdin.readline()
    N, g = map(int, line.split())

    for i in range(int(N)):
        line = sys.stdin.readline()
        D, theta = map(float, line.split())
        if i == 0:
            v = math.sqrt(2 * g * D * math.cos(math.radians(theta)))
            print("%.2f" % v)
        else:
            v = math.sqrt(2 * g * D * math.cos(math.radians(theta)) + v ** 2)
            print("%.2f" % v)

if __name__ == "__main__":
    main()
