
N = int(input())
A = list(map(int, input().split()))

N = 6
A = [1, 2, 1, 2, 1, 2]

# N = 5
# A = [1, 2, 1, 2, 1]

# N = 3
# A = [1, 1, 1]

# N = 2
# A = [1, 1]

# def check(A):
#     i = 0
#     while i < N:
#         if A[i] % 2 == 0:
#             i += 1
#         else:
#             return False
#     return True

# if check(A):
#     print(0)
#     exit()

A.sort()

# i = 0
# while i < N:
#     if A[i] % 2 == 0:
#         i += 1
#     else:
#         break

# if i == N:
#     print(0)
#     exit()

# ans = 0
# if i % 2 == 0:
#     ans = A[i]
# else:
#     ans = A[i-1]

# print(ans)
