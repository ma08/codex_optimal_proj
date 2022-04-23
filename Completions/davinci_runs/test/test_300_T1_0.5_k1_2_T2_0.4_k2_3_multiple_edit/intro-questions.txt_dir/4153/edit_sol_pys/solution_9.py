import sys
import math


def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    max_a = a[-1]
    min_a = a[0]
    ans = math.inf
    for i in range(min_a, max_a + 1):
        cost = 0
        for j in range(n):
            cost += (a[j] - i) ** 2
        ans = min(ans, cost)
    print(ans)


if __name__ == '__main__':
    main()
