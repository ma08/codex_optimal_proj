

N = int(input())  # 人数
A = [0] + list(map(int, input().split()))  # 各人の所有する色

ans = list(range(N + 1))
for i in range(1, N + 1):
    ans[A[i]] += 1

for i in range(1, N + 1):
    print(ans[i])
