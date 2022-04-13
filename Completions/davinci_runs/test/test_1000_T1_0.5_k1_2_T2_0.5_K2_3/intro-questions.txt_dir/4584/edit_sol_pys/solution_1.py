
N = int(input()) # 数列の長さ
A = [0] + list(map(int, input().split())) # 数列

ans = list(range(N + 1))
for i in range(1, N + 1):
    ans[A[i]] += 1

for i in range(1, N + 1):
    print(ans[i])
