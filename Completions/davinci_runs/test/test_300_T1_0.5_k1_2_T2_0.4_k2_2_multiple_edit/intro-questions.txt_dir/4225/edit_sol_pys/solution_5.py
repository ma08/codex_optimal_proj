

# A, B, K = map(int, input().split())  # 標準入力
A, B, K = 2, 1, 3  # テスト用

if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A - (K - A - B))
