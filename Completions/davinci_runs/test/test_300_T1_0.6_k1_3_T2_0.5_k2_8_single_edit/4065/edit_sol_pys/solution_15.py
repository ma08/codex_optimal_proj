

# def getMaxContest(a):
#     n = len(a)
#     dp = [1] * n
#     for i in range(n):
#         for j in range(i):
#             if a[i] <= 2 * a[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return max(dp)

# a = list(map(int, input().split()))
# print(getMaxContest(a))


def getMaxContest(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] <= 2 * arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


arr = list(map(int, input().split()))
print(getMaxContest(arr))
