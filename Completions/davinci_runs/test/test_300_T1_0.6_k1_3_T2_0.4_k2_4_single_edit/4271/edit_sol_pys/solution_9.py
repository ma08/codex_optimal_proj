

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

points = 0
for i in range(N-1):
    if A[i+1] - A[i] == 1: #if the next element is the next number
        points += (B[A[i]-1] + C[A[i]-1]) #add the points from the current element and the next element
    else:
        points += B[A[i]-1] #add the points from the current element
points += B[A[N-1]-1] #add the points from the last element
print(points)
