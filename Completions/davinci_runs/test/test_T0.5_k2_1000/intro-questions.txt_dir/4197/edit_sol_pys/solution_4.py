
N = int(input())
A = [int(i) for i in input().split()]

for i in range(N):
    print(A.index(i+1)+1)
