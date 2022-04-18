

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for a in A:
    for i in range(D):
        if (i + 1) % a == 0:
            X += 1

for i in range(1, D + 1):
    if i % A[0] == 0:
        X += 1

print(X)
