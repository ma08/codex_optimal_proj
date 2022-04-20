

N, L = map(int, input().split())

# 1からNまでの合計
Sum = int(N * (N + 1) / 2)

# 絶対値の小さい方の値を出力
if abs(L) <= abs(L + N - 1):
    print(Sum + L)
else:
    print(Sum + L + N - 1)