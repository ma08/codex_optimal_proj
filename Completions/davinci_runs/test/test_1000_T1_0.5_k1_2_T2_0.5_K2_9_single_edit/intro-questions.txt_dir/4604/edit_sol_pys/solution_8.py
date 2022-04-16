import numpy as np

N = int(input())
A = list(map(int, input().split()))

if A[0] != 0:
    print(0)
    exit()

if len(set(A)) != N:
    print(0)
    exit()

s = []
for i in range(N):
    if len(s) == 0:
        s.append(i+1)
        continue
    if A[i] >= len(s):
        s.append(i+1)
    else:
        s.insert(A[i], i+1)

ans = np.prod(s) % (10**9 + 7)
print(ans)
