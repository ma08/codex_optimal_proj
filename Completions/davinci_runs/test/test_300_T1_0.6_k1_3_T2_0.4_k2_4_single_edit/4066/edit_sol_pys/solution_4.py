

def solve(a):
    # Write your code here
    n = len(a)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if j == i:
                dp[i][j] = a[i]
            else:
                dp[i][j] = dp[i][j - 1] ^ a[j]

    return dp

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))

if __name__ == '__main__':
    main()
