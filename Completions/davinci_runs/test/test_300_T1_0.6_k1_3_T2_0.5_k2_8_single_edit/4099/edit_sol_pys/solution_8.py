# coding: utf-8


# S = sum(Ai)
# S + x = M * N
# x = M * N - S

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)

if M * N - S < 0:
    print(-1)
elif M * N - S > K:
    print(-1)
else:
    print(M * N - S)
