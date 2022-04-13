

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(N):
    X += (D - 1) // A[i] + 1
print(X)
