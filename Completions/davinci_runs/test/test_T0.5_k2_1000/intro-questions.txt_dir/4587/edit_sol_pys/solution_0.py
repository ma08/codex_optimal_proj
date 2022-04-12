from bisect import bisect_right


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0

for i in range(N):
    a = bisect_right(B, A[i] + 1)
    c = bisect_right(C, B[a - 1] + 1)
    ans += a * c

print(ans)
