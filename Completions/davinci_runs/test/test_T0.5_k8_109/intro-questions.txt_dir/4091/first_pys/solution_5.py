

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for j in range(1, k+1):
        for i in range(1, n+1):
            if j == 1:
                dp[j][i] = arr[i-1]
            else:
                max_val = -1
                for l in range(i):
                    max_val = max(max_val, dp[j-1][l] + max(arr[l:i]))
                dp[j][i] = max_val

    print(dp[k][n])
    i = n
    j = k
    while j > 0:
        while dp[j][i] == dp[j][i-1]:
            i -= 1
        print(i, end=' ')
        j -= 1
        i -= 1
    print()


if __name__ == '__main__':
    main()