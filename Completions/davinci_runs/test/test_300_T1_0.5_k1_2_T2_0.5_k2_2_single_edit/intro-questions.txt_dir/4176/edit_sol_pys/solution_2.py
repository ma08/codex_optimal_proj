import math

sys.setrecursionlimit(10 ** 7)
import sys

def main():
    # input
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    a.reverse()
    # solve
    ans = 0
    for i in range(n):
        ans = max(ans, min(i + 1, a[i]))
    # output
    print(ans)

if __name__ == '__main__':
    main()
