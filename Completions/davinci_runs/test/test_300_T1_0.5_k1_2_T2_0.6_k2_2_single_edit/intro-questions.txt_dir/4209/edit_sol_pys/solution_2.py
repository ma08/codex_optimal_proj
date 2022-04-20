"""
Find the maximum length of a subsequence such that elements in the subsequence are consecutive integers, the
consecutive numbers can be in any order. A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For example, the sequence
[1, 3, 4] is a subsequence of [1, 2, 3, 4] and [4, 1, 5, 3, 2] but not a subsequence of [1, 2, 4].
"""

import sys

def solve(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if a[i] == a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(a)
    print(max(dp))
    for i, d in enumerate(dp):
        if d == max(dp):
            print(i - d + 2, i + 1)

if __name__ == '__main__':
    main()
