
A,B = input().split()
N = len(A)
M = len(B)

for i in range(N):
    if A[i] in B:
        break
print('.'*(B.index(A[i])) + A[i] + '.'*(M-B.index(A[i])-1))
for j in range(N-1):
    print('.'*N)
print(B)
for k in range(N-i-1):
    print('.'*N)
