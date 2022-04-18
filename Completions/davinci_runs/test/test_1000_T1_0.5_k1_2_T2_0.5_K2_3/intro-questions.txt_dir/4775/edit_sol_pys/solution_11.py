
A,B = input().split()
N = len(A)
M = len(B)

for i in range(M-1):
    if B[i] in A:
        break

print('.'*(N-1) + B[i+1])
for j in range(i):
    print('.'*(A.index(B[j])) + B[j] + '.'*(N-A.index(B[j])-1))
print(A)
for k in range(M-i-2):
    print('.'*N)
