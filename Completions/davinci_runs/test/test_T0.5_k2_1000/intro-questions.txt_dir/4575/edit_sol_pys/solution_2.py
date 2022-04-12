
N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(1, D + 1):
    if i in A:
        X += 1

print(X)
