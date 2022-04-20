
import sys

def solve(n, a):
    """
    >>> solve(7, [4, 1, 2, 2, 1, 5, 3])
    3
    7 7
    2 3
    4 5
    >>> solve(11, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    2
    3 4
    1 1
    >>> solve(4, [1, 1, 1, 1])
    4
    4 4
    1 1
    2 2
    3 3
    """
    sums = [0] * (n+1)
    for i in range(n):
        sums[i+1] = sums[i] + a[i]
    # print(sums)
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]
        for j in range(1, i):
            if sums[i] - sums[j] == 0:
                dp[i] = max(dp[i], dp[j]+1)
    # print(dp)
    print(dp[n])
    i = n
    while i > 0:
        for j in range(i-1, 0, -1):
            if sums[i] - sums[j] == 0:
                if dp[i] == dp[j]+1:
                    print(j, i)
                    i = j
                    break
        if i > 0:
            print(i, i)
            i = 0

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, a)
