

# N, M = map(int, input().split())
# L = []
# R = []
# for _ in range(M):
#     l, r = map(int, input().split())
#     L.append(l)
#     R.append(r)

# L_min = min(L)
# R_max = max(R)
# print(R_max - L_min + 1)

# N, A, B = map(int, input().split())
# X = list(map(int, input().split()))
# ans = 0
# for i in range(1, N):
#     d = X[i] - X[i - 1]
#     if d * A > B:
#         ans += B
#     else:
#         ans += d * A
# print(ans)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort()
# B.sort()
# ans = 0
# for a in A:
#     for b in B:
#         if a < b:
#             ans += 1
#             B.remove(b)
#             break
# print(ans)


# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for _ in range(N):
#     a = A.pop(0)
#     if a % 2 == 0:
#         ans += 1
#         A = [a // 2 for a in A]
# print(ans)


# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort()
# B.sort(reverse=True)
# ans = 0
# for a, b in zip(A, B):
#     ans += a * b
# print(ans)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort(reverse=True)
# B.sort()
# ans = 0
# for a, b in zip(A, B):
#     ans += a * b
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     if a < 0:
#         ans += 1
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# ans = 0
# for i in range(1, N):
#     ans += A[i] - A[i - 1]
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# ans = 0
# for i in range(1, N):
#     ans += A[i] - A[i - 1]
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# ans = 0
# for i in range(1, N):
#     ans += A[i] - A[i - 1]
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     ans += a - 1
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     ans += a - 1
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     ans += a - 1
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     ans += a - 1
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     ans += a - 1
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for a in A:
#     ans += a - 1
# print(ans)
