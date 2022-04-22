

N = int(input())

A = list(map(int, input().split()))

L = []
R = []

for i in range(N):
    if i == 0:
        L.append(0)
    else:
        L.append(L[i-1] + A[i-1])

for i in range(N-1, -1, -1):
    if i == N - 1:
        R.append(0)
    else:
        R.append(R[0] + A[i+1])

R.reverse()

ans = float("inf")
for i in range(N):
    ans = min(ans, abs(L[i] - R[i]))

print(ans)
