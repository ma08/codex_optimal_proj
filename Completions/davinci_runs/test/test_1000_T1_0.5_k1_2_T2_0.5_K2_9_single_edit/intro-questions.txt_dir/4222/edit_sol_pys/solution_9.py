

# input
N, K = map(int, input().split())

# get inputs
A = []
for i in range(K):
    d = int(input())
    A.append(list(map(int, input().split())))
# flatten list

A_flat = []
for i in range(K):
    A_flat.extend(A[i])
A_flat = set(A_flat)
# calculate

ans = N - len(A_flat)
print(ans)
