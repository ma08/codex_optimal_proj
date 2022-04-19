N, K = map(int, input().split())
A = list(map(int, input().split()))


# 累積和を求める
s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]

# 2次元配列にまとめる
A_list = []
for i in range(N):
    A_list.append([A[i], i])

# 小さい順にソートする
A_list.sort(key=lambda x:x[0])

# 最小値と最大値の絶対値を求める
min_value = A_list[0][1]
max_value = A_list[-1][1]

print(max(max_value-min_value, N-1-min_value+max_value))
