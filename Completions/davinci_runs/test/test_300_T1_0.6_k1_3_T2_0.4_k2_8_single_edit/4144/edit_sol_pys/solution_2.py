#

N = int(input())

# A[i] = the number of ways to make a sequence of length i that satisfies all conditions
# A[i] = A[i-1] + A[i-2]
# A[i] = A[i-2] + A[i-3] + \cdots + A[0]
# A[i] = A[i-1] + A[i-1] - A[0]
# A[i] = 2*A[i-1] - A[0]
#
# A[0] = 1
# A[1] = 2
A = [0]*(N+1)
A[0] = 1
A[1] = 2
for i in range(2,N+1):
    A[i] = (2*A[i-1] - A[0])%(10**9+7)
print(A[N])
