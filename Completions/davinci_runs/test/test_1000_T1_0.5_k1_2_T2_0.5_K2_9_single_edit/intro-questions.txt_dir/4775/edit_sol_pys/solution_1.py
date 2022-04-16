

A, B = input().split()
N = len(A)
M = len(B)

for i in range(M):
    if B[i] in A:
        break

print('.'*(N-1) + B[i], end='')
for j in range(M-1):
    print('.'*(A.index(B[i])) + B[i] + '.'*(N-A.index(B[i])-1), end='')
print(A, end='')
for k in range(M-i-1):
    print('.'*N, end='')
