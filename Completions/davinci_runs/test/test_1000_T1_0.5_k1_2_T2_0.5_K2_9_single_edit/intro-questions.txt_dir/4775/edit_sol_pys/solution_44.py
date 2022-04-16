

A, B = input().split()
N, M = len(A), len(B)

for i in range(M):
    if B[i] in A:
        break

print('.' * (N - 1) + B[i])
for j in range(M - 1):
    print('.' * (A.index(B[i])) + B[i] + '.' * (N - A.index(B[i]) - 1))
print(A)
for k in range(M - i - 1):
    print('.' * N)
