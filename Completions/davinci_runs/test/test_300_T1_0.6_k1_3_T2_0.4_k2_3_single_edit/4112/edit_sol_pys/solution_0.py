

def solve(n, k, x, a):
    if x == 0:
        return 0
    if n == k:
        return sum(a)
    dp = [[[-1 for _ in range(x+1)] for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            if i+j >= n:
                break
            dp[i][j][1] = sum(a[i:i+j+1])
    for i in range(n):
        for j in range(k):
            if i+j >= n:
                break
            for l in range(2, x+1):
                for m in range(i+j+1, n):
                    if j+m-i+1 >= k:
                        dp[i][j][l] = max(dp[i][j][l], sum(a[i:i+j+1])+dp[m][j+m-i+1-k][l-1])
    return max([max(x) for x in dp[0][0]])

if __name__ == '__main__':
    n,k,x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    print(solve(n,k,x,a))
