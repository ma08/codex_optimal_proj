
def get_expected(n, k, dp):
    if k == 1:
        return n/2
    if n == 1:
        return 1
    if dp[n][k] != -1:
        return dp[n][k]
    dp[n][k] = (n/2) + get_expected(n, k-1, dp)
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    dp = [[-1 for i in range(k+1)] for j in range(n+1)]
    print(get_expected(n, k, dp))

if __name__ == '__main__':
    main()
