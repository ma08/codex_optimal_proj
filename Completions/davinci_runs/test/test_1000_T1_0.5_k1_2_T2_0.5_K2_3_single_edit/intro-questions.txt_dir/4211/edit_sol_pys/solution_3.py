

#N = int(input())
#B = list(map(int,input().split()))
N = 3
B = [2,5,4]

#A = [0]*N
A = [0]*N

A[0] = min(B[0],B[1])
A[-1] = min(B[-2],B[-1])

for i in range(1,N-1):
    A[i] = min(B[i],B[i-1],A[i-1])

print(sum(A))
