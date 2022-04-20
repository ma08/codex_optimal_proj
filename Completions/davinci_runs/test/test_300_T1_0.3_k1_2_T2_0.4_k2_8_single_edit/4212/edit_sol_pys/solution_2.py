# 入力
N, A, B = map(int, input().split())


# 処理
if A * N > B:
    print(B)
else:
    print(A * N)
