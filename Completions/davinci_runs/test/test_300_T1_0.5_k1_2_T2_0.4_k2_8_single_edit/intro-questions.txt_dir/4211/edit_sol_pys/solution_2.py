

#N = int(input())
#B = list(map(int,input().split()))
N = 5
B = [4,9,2,4,7]

#A = [0]*N
A = [0]*N

A[0] = B[0]
A[-1] = B[-1]

for i in range(1,N-1):
    A[i] = B[i] - A[i-1]

print(sum(A))
