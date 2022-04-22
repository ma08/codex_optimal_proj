

N = int(input())
B = list(map(int,input().split()))
#N = 3
#B = [2,5]

#A = [0]*N
A = [0]*N

A[0] = B[0]
A[-1] = B[-1]

for i in range(1,N-1):
    A[i] = B[i] - A[i-1]

print(sum(A))
