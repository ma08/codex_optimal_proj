

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

points = 0
for i in range(N-1):
    if A[i+1] - A[i] == 1: # if next number is consecutive
        points += (B[A[i]-1] + C[A[i]-1]) # add both points
    else:
        points += B[A[i]-1] # add only first point
points += B[A[N-1]-1] # add last point
print(points)
