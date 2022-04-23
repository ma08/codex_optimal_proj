N = int(input())
A = [int(i) for i in input().split()]

for i in range(N):
    print(A[i], end="")
    if i != N - 1:
        print(" ", end="")
