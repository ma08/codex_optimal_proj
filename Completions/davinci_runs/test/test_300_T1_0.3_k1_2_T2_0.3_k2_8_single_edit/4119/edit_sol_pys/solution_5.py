

import sys

def main():
    # read input
    n, m = map(int, input().split())
    x = list(map(int, input().split()))[:m]

    # sort the coordinates
    x.sort()

    # find the minimum number of moves required to achieve the objective
    ans = sum(abs(x[i] - x[i-1]) for i in range(m))
    print(ans)

if __name__ == '__main__':
    main()
