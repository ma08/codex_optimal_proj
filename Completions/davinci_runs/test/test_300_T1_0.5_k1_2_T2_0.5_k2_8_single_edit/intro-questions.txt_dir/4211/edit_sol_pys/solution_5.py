

N = int(input())
B = list(map(int,input().split()))
#N = 3
#B = [2,5]

A = [0]*N

A[0] = B[0]
A[-1] = B[-1]

for i in range(N-2):
    A[i+1] = B[i] - A[i]

print(sum(A))
