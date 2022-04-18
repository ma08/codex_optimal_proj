# https://codeforces.com/contest/1183/problem/A

# # input
# a, b, c = input().split()

# # check
# if a[-1] == b[0] and b[-1] == c[0]:
#     print("YES")
# else:
#     print("NO")

# https://codeforces.com/contest/1183/problem/B

# # input
# n = int(input())

# # check
# if n < 3:
#     print(0)
# else:
#     print(int((n-2)*(n-1)*n/6))

# https://codeforces.com/contest/1183/problem/C

# # input
# n = int(input())
# a = list(map(int, input().split()))

# # check
# if a[0] == 1 or a[-1] == 1:
#     print(-1)
# else:
#     for i in range(1, n-1):
#         if a[i] == 1 and a[i-1] != 1 and a[i+1] != 1:
#             print(i+1)
#             break

# https://codeforces.com/contest/1183/problem/D

# # input
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# # check
# if n == 1:
#     print(a[0] + k)
#     exit()
# a.sort()
# if k == 0:
#     print(a[0])
#     exit()
# if k >= a[-1] - a[0]:
#     print(a[-1])
#     exit()
# i = 0
# while k > 0:
#     if a[i+1] - a[i] <= k:
#         k -= a[i+1] - a[i]
#         a[i] = a[i+1]
#     else:
#         a[i] += k
#         k = 0
# print(a[i])

# https://codeforces.com/contest/1183/problem/E

# # input
# n = int(input())
# a = list(map(int, input().split()))

# # check
# if n == 1:
#     print(a[0], a[0])
#     exit()
# if n == 2:
#     print(a[1], a[0])
#     exit()
# a.sort()
# res = []
# for i in range(n):
#     res.append(a[i])
#     if i % 2 == 1:
#         res.append(a[i])
# if n % 2 == 0:
#     res.append(a[0])
# print(*res[::-1])

# https://codeforces.com/contest/1183/problem/F

# # input
# n = int(input())
# a = list(map(int, input().split()))

# # check
# a.sort()
# res = []
# for i in range(n):
#     res.append(a[i])
#     if i % 2 == 1:
#         res.append(a[i])
# if n % 2 == 0:
#     res.append(a[0])
# print(*res[::-1])
