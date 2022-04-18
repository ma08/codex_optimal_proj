
N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
for i in range(1, N + 1):
    ans[A[i]] += 1

for i in range(1, N + 1):
    print(ans[i])
