

# n = int(input())
# s = input()

# def solve(n, s):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1 if s[0] <= s[1] else 2

#     start = 0
#     cur = 0
#     res = 0
#     for i in range(1, n):
#         if s[i] < s[i - 1]:
#             cur += 1
#             res = max(res, cur)
#         else:
#             cur = 0
            
#     return res + 1

# print(solve(n, s))


# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# def solve(N, K, A):
#     if K == 0:
#         return " ".join(map(str, A))
#     if K == 1:
#         return " ".join(map(str, sorted(A)))
#     if K % 2 == 0:
#         return " ".join(map(str, sorted(A)))
#     else:
#         return " ".join(map(str, sorted(A, reverse=True)))

# print(solve(N, K, A))


# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# def solve(n, a, b):
#     a = sorted(a)
#     b = sorted(b, reverse=True)
#     res = 0
#     for i in range(n):
#         res += a[i] * b[i]
    
#     return res

# print(solve(n, a, b))


# n = int(input())
# a = list(map(int, input().split()))

# def solve(n, a):
#     a = sorted(a)
#     res = 0
#     for i in range(n - 1):
#         res += a[i]
    
#     res += a[-1] // 2

#     return res

# print(solve(n, a))


# n = int(input())
# a = list(map(int, input().split()))

# def solve(n, a):
#     a = sorted(a)
#     res = 0
#     for i in range(n - 1):
#         res += a[i]
    
#     res += a[-1] // 2

#     return res

# print(solve(n, a))


# n = int(input())
# a = list(map(int, input().split()))

# def solve(n, a):
#     a = sorted(a)
#     res = 0
#     for i in range(n - 1):
#         res += a[i]
    
#     res += a[-1] // 2

#     return res

# print(solve(n, a))


# n = int(input())
# s = input()

# def solve(n, s):
#     if n % 2 == 1:
#         return 0
#     elif s[:n // 2] == s[n // 2:]:
#         return n // 2
#     else:
#         return 0

# print(solve(n, s))


# n = int(input())
# s = input()

# def solve(n, s):
#     if n % 2 == 1:
#         return 0
#     elif s[:n // 2] == s[n // 2:]:
#         return n // 2
#     else:
#         return 0

# print(solve(n, s))


# n = int(input())
# s = input()

# def solve(n, s):
#     if n % 2 == 1:
#         return 0
#     elif s[:n // 2] == s[n // 2:]:
#         return n // 2
#     else:
#         return 0

# print(solve(n, s))
