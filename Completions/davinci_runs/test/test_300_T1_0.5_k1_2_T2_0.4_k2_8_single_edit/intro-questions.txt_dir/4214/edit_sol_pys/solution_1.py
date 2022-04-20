

N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == K:
    print(1)
    exit()

A.sort()
if A[0] == 0:
    print(0)
    exit()

ans = 1
for i in range(N-1):
    if A[i]*2 <= A[i+1]:
        ans += 1

print(ans)
