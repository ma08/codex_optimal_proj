
N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for a in A:
    X += 1 + (D - 1) // a

print(X)
