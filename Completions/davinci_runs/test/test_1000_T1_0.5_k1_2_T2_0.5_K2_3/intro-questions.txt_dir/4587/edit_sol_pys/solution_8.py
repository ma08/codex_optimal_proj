
N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0

for i in range(N):
    a = bisect_left(B, A[i] + 1)
    c = bisect_left(C, B[i] + 1)
    ans += a * c

print(ans)
