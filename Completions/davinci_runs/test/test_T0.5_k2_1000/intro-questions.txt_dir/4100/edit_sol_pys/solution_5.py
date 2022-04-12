N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    ans += B[A[i] - 1]
    if i > 0 and A[i] - A[i-1] == 1:
        ans += C[A[i-1] - 1]
print(ans)
