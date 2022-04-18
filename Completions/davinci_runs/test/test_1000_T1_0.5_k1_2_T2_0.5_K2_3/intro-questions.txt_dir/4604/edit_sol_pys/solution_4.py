

N = int(input())
A = list(map(int, input().split()))

if A[0] != 0:
    print(0)
    exit()

if len(set(A)) != N:
    print(0)
    exit()

S = []
for i in range(N):
    if len(S) == 0:
        S.append(i+1)
        continue
    if A[i] >= len(S):
        S.append(i+1)
    else:
        S.insert(A[i], i+1)

for i in range(N):
    print(S[i])
