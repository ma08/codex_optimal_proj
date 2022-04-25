

N = int(input())
A = list(map(int, input().split()))

# 2次元配列にまとめる(値とインデックスを格納) 
A_list = []
for i in range(N):
    A_list.append([A[i], i])

# 小さい順にソートする(インデックスは値と一緒にソートされる)
A_list.sort(key=lambda x:x[0])

# 最小値と最大値の絶対値を求める
min_value = A_list[0][1]
max_value = A_list[-1][1]

print(max(max_value-min_value, N-1-min_value+max_value))
