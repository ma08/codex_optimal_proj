

#N = int(input())
#B = list(map(int,input().split()))
N = 5
B = [9,20,18,13,19]

#A = [0]*N
A = [0]*N

A[0] = min(B[0],B[1])
A[-1] = min(B[-1],B[-2])

for i in range(1,N-1):
    A[i] = min(B[i],B[i-1],B[i+1])


print(sum(A))
