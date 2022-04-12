

A, B, C, K = map(int, input().split())  # 入力
# A, B, C, K = 2, 1, 1, 3  # 入力

if K <= A:
    print(K)  # 出力
elif K <= A+B:
    print(A)  # 出力
else:
    print(A - (K - A - B))  # 出力
