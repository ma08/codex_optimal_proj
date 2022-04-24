

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

points = 0
for i in range(N-1):
    if A[i+1] - A[i] == 1: # if the next number is 1 more than the previous
        points += (B[A[i]-1] + C[A[i]-1]) # add the two points of the two numbers
    else:
        points += B[A[i]-1] # if the next number is not 1 more than the previous
points += B[A[N-1]-1] # add the last number's points
print(points)
