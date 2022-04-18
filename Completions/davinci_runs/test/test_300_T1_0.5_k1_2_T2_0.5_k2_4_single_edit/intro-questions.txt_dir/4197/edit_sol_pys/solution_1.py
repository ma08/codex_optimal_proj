

N = int(input())
A = [int(i) for i in input().split()]

for i in range(1, N + 1):
    print(A.index(i) + 1, end=' ')
