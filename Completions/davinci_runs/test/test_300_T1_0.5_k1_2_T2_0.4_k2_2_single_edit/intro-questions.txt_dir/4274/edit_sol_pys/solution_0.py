
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(0, N-1, 2):
    ans += A[i+1] - A[i]
print(ans)
