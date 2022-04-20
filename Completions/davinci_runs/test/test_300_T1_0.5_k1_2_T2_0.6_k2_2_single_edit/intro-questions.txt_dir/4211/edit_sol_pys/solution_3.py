

#N = int(input())
#B = list(map(int,input().split()))
N = 2
B = [3,4]

#A = [0]*N
A = [0]*N

A[0] = B[0]
A[-1] = B[-1]

for i in range(1,N-1):
    if B[i] - A[i-1] >= 0:
        A[i] = B[i] - A[i-1]
    else:
        print(-1)
        exit()

print(sum(A))
