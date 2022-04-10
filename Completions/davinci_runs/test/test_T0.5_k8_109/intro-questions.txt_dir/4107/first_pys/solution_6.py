

import sys

def main():
    # read input
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    # find the number of routers needed
    routers_needed = 0
    for i in range(n):
        if s[i] == '0' and i + 1 > k:
            routers_needed += 1
    # find the minimum cost
    cost = 0
    for i in range(n):
        if s[i] == '1':
            cost += min(i + 1, n - i, n - routers_needed)
        else:
            cost += i + 1
    print(cost)

if __name__ == '__main__':
    main()