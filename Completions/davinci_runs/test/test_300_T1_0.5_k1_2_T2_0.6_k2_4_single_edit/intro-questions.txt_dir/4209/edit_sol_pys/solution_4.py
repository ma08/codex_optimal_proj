

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
    dp = [1] * (n+1)
    dp[1] = 1
    for i in range(2, n+2):
        dp[i] = 1
        for j in range(1, i):
            if sums[i] == sums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    # print(dp)
    print(dp[n])
    i = n+1
    while i > 1:
        j = i-2
        while j > 0:  # j >= 0
            if sums[i-1] == sums[j] and dp[i] == dp[j]+1:
                print(j, i-1)
                i = j+1
                break
            j -= 1
        else:
            print(i-1, i-1)
            i -= 1  # i = i-1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, a)
