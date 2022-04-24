
for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if n == k:
        print(sum(a))
    else:
        for i in range(k):
            a.append(a[i])
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i+j >= n:
                    break
                dp[i][j] = sum(a[i:j+1])
        max_sum = -1
        for i in range(n):
            for j in range(n):
                if i+j >= n:
                    break
                max_sum = max(max_sum, dp[i][j])
        print(max_sum)
