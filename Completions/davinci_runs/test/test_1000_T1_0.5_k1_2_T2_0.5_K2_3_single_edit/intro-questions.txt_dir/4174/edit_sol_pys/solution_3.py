


# N, X = map(int, input().split())
# L = list(map(int, input().split()))

# cnt = 1
# dist = 0
# for i in range(N):
#     dist += L[i]
#     if dist <= X:
#         cnt += 1
#     else:
#         break
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1] == A[i]-1:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N, M = map(int, input().split())
# H = list(map(int, input().split()))
# AB = [[int(i) for i in input().split()] for _ in range(M)]

# cnt = 0
# for i in range(M):
#     if H[AB[i][0]-1] == H[AB[i][1]-1]:
#         cnt += 1

# print(M-cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1] == A[i]-1:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1] == A[i]-1:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1] == A[i]-1:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1] == A[i]-1:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1] == A[i]-1:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# cnt = 0
# for i in range(N):
#     cnt += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             cnt += C[A[i-1]-1]
# print(cnt)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(

N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
dist = 0
for i in range(N):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break
print(cnt)
