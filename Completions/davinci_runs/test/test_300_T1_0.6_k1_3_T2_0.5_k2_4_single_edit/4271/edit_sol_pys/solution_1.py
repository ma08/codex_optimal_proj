

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

points = 0
for i in range(N):
    points += B[A[i]-1]
    if i != N-1 and A[i+1] - A[i] == 1:
        points += C[A[i]-1]
print(points)
