
N, K = map(int, input().split())  # N, Kをint型に変換

if N % K == 0:
    print(0)  # 割り切れる場合は0
else:
    print(1)
