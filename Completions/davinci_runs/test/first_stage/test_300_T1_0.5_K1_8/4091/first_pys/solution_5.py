

def solve(arr, k):
    if k == 1:
        return sum(arr)
    if k == len(arr):
        return max(arr)
    dp = [[0 for _ in range(len(arr)+1)] for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(i, len(arr)+1):
            if i == 1:
                dp[i][j] = sum(arr[:j])
            else:
                m = 0
                for l in range(j-1, i-2, -1):
                    m = max(m, dp[i-1][l])
                    dp[i][j] = max(dp[i][j], m+sum(arr[l:j]))
    return dp[k][len(arr)]

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, k))

if __name__ == '__main__':
    main()