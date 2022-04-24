

#N = int(input())
#B = list(map(int,input().split()))

#A = [0]*(N+1)
#A[0] = B[0]
#A[-1] = B[-1]

#for i in range(1,N):
#    A[i] = B[i] - A[i-1]

#print(sum(A))

N = int(input()) #2
B = list(map(int,input().split())) #[1,2]
A = [0]*(N+1)
A[0] = B[0] #[1,0]
A[-1] = B[-1] #[1,2]
for i in range(1,N):
    A[i] = B[i] - A[i-1] #[1,1]
print(sum(A)) #2
