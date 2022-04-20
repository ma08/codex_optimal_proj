

N, M = map(int, input().split())

A = []
B = []
C = []
D = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(a)
    D.append(b)

A.sort()
B.sort()

for i in range(M):
    a = A.index(C[i])
    b = M - B.index(D[i]) - 1
    print(a + b)
