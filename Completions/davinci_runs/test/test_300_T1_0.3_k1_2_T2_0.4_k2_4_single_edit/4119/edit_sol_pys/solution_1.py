

import sys

def main():
    # read input
    m, n = map(int, input().split())
    x = list(map(int, input().split()))

    # sort the coordinates
    x.sort()

    # find the minimum number of moves required to achieve the objective
    ans = 0 # initialize answer
    for i in range(m):
        ans += abs(x[i] - x[i-1]) # add the absolute difference between adjacent elements
    print(ans)

if __name__ == '__main__':
    main()
