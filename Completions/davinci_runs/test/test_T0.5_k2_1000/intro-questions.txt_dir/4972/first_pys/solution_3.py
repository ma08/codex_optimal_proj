

import sys
import math

def main():
    X = int(sys.stdin.readline())
    k = int(math.log(X, 2))
    print(k)

if __name__ == "__main__":
    main()