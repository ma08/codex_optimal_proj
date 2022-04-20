
N = int(input())
A = list(map(int, input().split()))

max_diff = 0
min_a = A[0]  # 最小値
for i in range(1, N):
    max_diff = max(max_diff, A[i]-min_a)  # 最大差分を更新
    min_a = min(min_a, A[i])  # 最小値を更新
print(max_diff)
