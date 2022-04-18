

A, B = input().split()
n = len(A)
m = len(B)

for i in range(m):
    if B[i] in A:
        break

print('.' * (n - 1) + B[i])
for j in range(m - 1):
    print('.' * (A.index(B[i])) + B[i] + '.' * (n - A.index(B[i]) - 1))
print(A)
for k in range(m - i - 1):
    print('.' * n)
