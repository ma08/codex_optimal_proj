

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    # see editorial for explanation
    # we can't get the answer directly, but we can get the answer on the reverse of the array
    # if we have the answer on the reverse of the array, we can get the answer on the original array
    # let's solve it on the reverse of the array

    # first, we need a function to calculate the number of different monotonic renumerations of an array
    # we can use a dynamic programming approach
    # let's say we have an array a[1..n]
    # let's say we have an array dp[1..n][0..n]
    # dp[i][j] is the number of different monotonic renumerations of a[1..i] such that the last number of the array is j
    # we can calculate dp[i][j] as follows:
    # if j > 0, then dp[i][j] = dp[i - 1][j - 1]
    # if j == 0 and a[i] == a[i - 1], then dp[i][j] = dp[i - 1][j]
    # if j == 0 and a[i] != a[i - 1], then dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
    # the answer is dp[n][0]
    # the complexity is O(n^2)

    # now we have the function to calculate the number of different monotonic renumerations of an array
    # let's use it to calculate the answer on the reverse of the array
    # we can use a dynamic programming approach
    # let's say we have an array a[1..n]
    # let's say we have an array dp[1..n][0..n]
    # dp[i][j] is the number of different monotonic renumerations of a[i..n] such that the first number of the array is j
    # we can calculate dp[i][j] as follows:
    # if j > 0, then dp[i][j] = dp[i + 1][j - 1]
    # if j == 0 and a[i] == a[i + 1], then dp[i][j] = dp[i + 1][j]
    # if j == 0 and a[i] != a[i + 1], then dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
    # the answer is dp[1][0]
    # the complexity is O(n^2)

    # now we have the answer on the reverse of the array
    # let's use it to calculate the answer on the original array
    # let's say we have an array a[1..n]
    # let's say we have an array dp[1..n][0..n]
    # dp[i][j] is the number of different monotonic renumerations of a[1..i] such that the last number of the array is j
    # we can calculate dp[i][j] as follows:
    # if j > 0, then dp[i][j] = dp[i - 1][j - 1]
    # if j == 0 and a[i] == a[i - 1], then dp[i][j] = dp[i - 1][j]
    # if j == 0 and a[i] != a[i - 1], then dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
    # the answer is dp[n][0]
    # the complexity is O(n^2)

    # now we have the answer on the original array
    # the complexity is O(n^2)

    # let's calculate the answer on the reverse of the array
    a = a[::-1]

    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    dp[n][0] = 1

    for i in range(n - 1, 0, -1):
        for j in range(n):
            if j > 0:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                if a[i] == a[i + 1]:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]

    answer = dp[1][0]

    # now we have the answer on the reverse of the array
    # let's use it to calculate the answer on the original array
    a = a[::-1]

    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    dp[n][0] = answer

    for i in range(n - 1, 0, -1):
        for j in range(n):
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if a[i] == a[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]

    answer = dp[1][0]

    # now we have the answer on the original array
    # the complexity is O(n^2)

    print(answer % 998244353)

if __name__ == '__main__':
    main()