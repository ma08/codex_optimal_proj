import sys
import math

if __name__ == "__main__":
    X = int(sys.stdin.readline())
    k = int(math.log(X, 2))
    print(k + 1)
