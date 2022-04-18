
import sys
import math
import numpy as np

def main():
    n = int(sys.stdin.readline())
    xs = list(map(int, sys.stdin.readline().split()))

    xs = np.array(xs)
    xs = np.sort(xs)

    ans = xs[0]
    for i in range(1, n):
        if xs[i] == xs[i-1]:
            ans -= 1

    print(ans)

if __name__ == "__main__":
    main()
