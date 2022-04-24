N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
ans = 0
prev = -1
for i in range(N):
    if prev == A[i] - 1:
        ans += C[A[i] - 1]
    ans += B[A[i] - 1]
    prev = A[i] - 1
print(ans)
