

# import sys

# sys.setrecursionlimit(10 ** 6)

# def dfs(v, parent = -1):
#     for u in g[v]:
#         if u != parent:
#             dfs(u, v)
#             dp1[v] += dp2[u]
#             dp2[v] += max(dp1[u], dp2[u])

# n = int(input())
# g = [set() for _ in range(n + 1)]
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     g[a].add(b)
#     g[b].add(a)

# dp1 = [0] * (n + 1)
# dp2 = [1] * (n + 1)
# dfs(1)

# print(max(dp1[1], dp2[1]))
# for v in range(1, n + 1):
#     if dp1[v] == max(dp1[1], dp2[1]) and v != 1:
#         print(1, v)
#         break
# for v in range(1, n + 1):
#     if dp2[v] == max(dp1[1], dp2[1]) and v != 1:
#         print(v)
#         break

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# if a[0] != 0:
#     print(0)
#     exit()
# ans = 1
# for i in range(n - 1):
#     if a[i] == a[i + 1]:
#         continue
#     else:
#         ans += 1
# print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# if a[0] != 0:
#     print(0)
#     exit()
# ans = 1
# for i in range(n - 1):
#     if a[i] == a[i + 1]:
#         continue
#     else:
#         ans += 1
# print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# if a[0] != 0:
#     print(0)
#     exit()
# ans = 1
# for i in range(n - 1):
#     if a[i] == a[i + 1]:
#         continue
#     else:
#         ans += 1
# print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# if a[0] != 0:
#     print(0)
#     exit()
# ans = 1
# for i in range(n - 1):
#     if a[i] == a[i + 1]:
#         continue
#     else:
#         ans += 1
# print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# if a[0] != 0:
#     print(0)
#     exit()
# ans = 1
# for i in range(n - 1):
#     if a[i] == a[i + 1]:
#         continue
#     else:
#         ans += 1
# print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# if a[0] != 0:
#     print(0)
#     exit()
# ans = 1
# for i in range(n - 1):
#     if a[i] == a[i + 1]:
#         continue
#     else:
#         ans += 1
# print(ans)
