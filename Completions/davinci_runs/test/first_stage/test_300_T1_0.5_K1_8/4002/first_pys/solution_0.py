

import sys

def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))

def read_single_int():
    return int(sys.stdin.readline().strip())

def main():
    n, m, k = read_list_int()
    a = []
    for _ in range(n):
        a.append(read_list_int())
    dp = [[0 for _ in range(k)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        for j in range(m):
            for l in range(k):
                dp[j][(l*10+a[i][j])%k] += dp[j-1][l]
    print(dp)

if __name__ == "__main__":
    main()