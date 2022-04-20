
#
# n = int(input())
# x = list(map(int, input().split()))
#
# x.sort()
#
# d = {}
# for i in range(n):
#     for j in range(i+1, n):
#         d[x[j] - x[i]] = d.get(x[j] - x[i], 0) + 1
#
# ans = []
# for i in range(n):
#     for j in range(i+1, n):
#         if d.get(x[j] - x[i], 0) > 1:
#             ans.append(x[i])
#             ans.append(x[j])
#             d[x[j] - x[i]] -= 2
#
# print(len(ans))
# print(*ans)
