

# n = input()
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = list(map(int,input().split()))

# ans = 0

# for i in range(len(a)):
#     ans += b[a[i]-1]
#     if i != 0 and a[i] == a[i-1] + 1:
#         ans += c[a[i-1]-1]

# print(ans)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dfs(c,v)
#         dp[v] += dp[c]

# n = int(input())
# tree = [[] for _ in range(n)]
# dp = [0 for _ in range(n)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     tree[a-1].append(b-1)
#     tree[b-1].append(a-1)
# for i in range(n):
#     dp[i] = int(input())

# dfs(0,-1)
# print(dp)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dfs(c,v)
#         dp[v] += dp[c]

# def dfs2(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dp2[c] = dp2[v] + dp[v] - dp[c] + (n-dp[c])
#         dfs2(c,v)

# n = int(input())
# tree = [[] for _ in range(n)]
# dp = [0 for _ in range(n)]
# dp2 = [0 for _ in range(n)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     tree[a-1].append(b-1)
#     tree[b-1].append(a-1)
# for i in range(n):
#     dp[i] = int(input())

# dfs(0,-1)
# dfs2(0,-1)
# print(dp2)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dfs(c,v)
#         dp[v] += dp[c]

# def dfs2(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dp2[c] = dp2[v] + dp[v] - dp[c] + (n-dp[c])
#         dfs2(c,v)

# n = int(input())
# tree = [[] for _ in range(n)]
# dp = [0 for _ in range(n)]
# dp2 = [0 for _ in range(n)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     tree[a-1].append(b-1)
#     tree[b-1].append(a-1)
# for i in range(n):
#     dp[i] = int(input())

# dfs(0,-1)
# dfs2(0,-1)
# print(dp2)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dfs(c,v)
#         dp[v] += dp[c]

# def dfs2(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dp2[c] = dp2[v] + dp[v] - dp[c] + (n-dp[c])
#         dfs2(c,v)

# n = int(input())
# tree = [[] for _ in range(n)]
# dp = [0 for _ in range(n)]
# dp2 = [0 for _ in range(n)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     tree[a-1].append(b-1)
#     tree[b-1].append(a-1)
# for i in range(n):
#     dp[i] = int(input())

# dfs(0,-1)
# dfs2(0,-1)
# print(dp2)

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dfs(c,v)
#         dp[v] += dp[c]

# def dfs2(v,p):
#     for c in tree[v]:
#         if c == p:
#             continue
#         dp2[c] = dp2[v] + dp[v] - dp[c] + (n-dp[c])
#         dfs2(c,v)

# n = int(input())
# tree = [[] for _ in range(n)]
# dp = [0 for _ in range(n)]
# dp2 = [0 for _ in range(n)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     tree[a-1].append(b-1)
#     tree[b-1].append(a-1)
# for i in range(n):
#     dp[i] = int(input())

# dfs(0,-1)
# dfs2(0,-1)
# print(dp2)
