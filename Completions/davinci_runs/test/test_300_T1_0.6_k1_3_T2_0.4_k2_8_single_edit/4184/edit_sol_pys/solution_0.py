
N = int(input())  # 数列の長さ
A = [int(x) for x in input().split(' ')]  # 数列
ans = 0
for i in range(N):
    for j in range(i, N):
        ans += A[i] * A[j]
print(ans)
