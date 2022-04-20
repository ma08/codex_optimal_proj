

import sys

def main():
    # read input
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    # sort the coordinates
    x.sort()

    # find the minimum number of moves required to achieve the objective
    ans = 0.0
    for i in range(m):
        ans += abs(x[i] - x[i - 1])
    print(ans)

if __name__ == '__main__':
    main()
