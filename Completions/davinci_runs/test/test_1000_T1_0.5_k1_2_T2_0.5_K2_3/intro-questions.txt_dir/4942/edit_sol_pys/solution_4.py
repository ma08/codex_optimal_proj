import sys
import math

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    while n > 0:
        n -= 1
        x = int(sys.stdin.readline())
        if x > 0:
            print(math.floor(math.log(x, 2)) + 1)
        else:
            print(0)
