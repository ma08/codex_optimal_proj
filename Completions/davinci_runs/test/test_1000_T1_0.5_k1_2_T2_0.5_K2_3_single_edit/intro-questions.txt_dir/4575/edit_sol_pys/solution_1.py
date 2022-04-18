
N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in A:
    X += (D - 1) // i + 1

print(X)
