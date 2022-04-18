
from collections import Counter
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
    >>> solve(5, [1, 1, 1, 1, 1])
    5
    5 5
    4 4
    3 3
    2 2
    1 1
    >>> solve(5, [1, 2, 3, 4, 5])
    1
    5 5
    >>> solve(3, [1, 2, 3])
    1
    3 3
    >>> solve(5, [1, 2, 3, 4, 5])
    1
    5 5
    >>> solve(5, [1, 2, 3, 4, 5])
    1
    5 5
    >>> solve(3, [1, 2, 3])
    1
    3 3
    >>> solve(4, [10, -10, 10, -10])
    4
    4 4
    3 3
    2 2
    1 1
    >>> solve(5, [1, 1, 1, 1, 1])
    5
    5 5
    4 4
    3 3
    2 2
    1 1
    >>> solve(5, [1, 1, 1, 1, 1])
    5
    5 5
    4 4
    3 3
    2 2
    1 1
    >>> solve(3, [1, 2, 3])
    1
    3 3
    >>> solve(4, [10, -10, 10, -10])
    4
    4 4
    3 3
    2 2
    1 1
    >>> solve(5, [1, 2, 3, 4, 5])
    1
    5 5
    >>> solve(5, [1, 1, 1, 1, 1])
    5
    5 5
    4 4
    3 3
    2 2
    1 1
    """
    sums = [0] * (n+1)
    for i in range(1, n+1):
        sums[i] = sums[i-1] + a[i-1]
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
        j = i-1
        while j > 0:
            if sums[i] - sums[j] == 0 and dp[i] == dp[j]+1:
                print(j, i)
                i = j
                break
            j -= 1
        else:
            print(i, i)
            i -= 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, a)
