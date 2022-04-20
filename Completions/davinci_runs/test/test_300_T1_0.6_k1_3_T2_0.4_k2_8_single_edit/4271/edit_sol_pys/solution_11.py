

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

points = 0
for i in range(N-1):
    if A[i+1] - A[i] == 1:
        points += (B[A[i]-1] + C[A[i]-1]) # add the points for the previous and current dish
    else:
        points += B[A[i]-1] # add the points for the previous dish
points += B[A[N-1]-1] # add the points for the last dish
print(points)
