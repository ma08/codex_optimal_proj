

# Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = a[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))

# dp = [0] * n
# dp[0] = a[0]
# for i in range(1, n):
#     dp[i] = max(dp[i-1] + a[i], a[i])

# print(max(dp))

# ans = [0] * k
# i = n - 1
# while i >= 0:
#     if i == n - 1:
#         ans[k-1] += 1
#     else:
#         if dp[i] == dp[i+1] + a[i]:
#             ans[k-1] += 1
#         else:
#             j = i + 1
#             while j < n and dp[j] == dp[j-1] + a[j]:
#                 j += 1
#             ans[k-1] += j - i
#             i = j - 1
#             k -= 1
#     i -= 1

# print(*ans)

# # dp = [0] * n
# # dp[0] = a[0]
# # for i in range(1, n):
# #     dp[i] = max(dp[i-1] + a[i], a[i])

# # print(max(dp))

# # ans = [0] * k
# # i = n - 1
# # while i >= 0:
# #     if i == n - 1:
# #         ans[k-1] += 1
# #     else:
# #         if dp[i] == dp[i+1] + a[i]:
# #             ans[k-1] += 1
# #         else:
# #             j = i + 1
# #             while j < n and dp[j] == dp[j-1] + a[j]:
# #                 j += 1
# #             ans[k-1] += j - i
# #             i = j - 1
# #             k -= 1
# #     i -= 1

# # print(*ans)