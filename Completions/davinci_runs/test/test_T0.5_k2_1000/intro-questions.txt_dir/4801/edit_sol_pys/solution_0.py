
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    dp = [A[0]]
    for i in range(1, n):
        if A[i] > dp[-1]:
            dp.append(A[i])
        else:
            for j in range(len(dp)):
                if dp[j] >= A[i]:
                    dp[j] = A[i]
                    break
    print(len(dp))
    print(*dp)

solve()
