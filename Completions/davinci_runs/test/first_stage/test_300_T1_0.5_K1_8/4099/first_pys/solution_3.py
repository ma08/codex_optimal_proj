

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

# 平均値を計算
ave = sum(a) / (n - 1)

# 平均値が目標を超える場合は-1を出力
if ave >= m:
    print(-1)

# 平均値が目標を超えない場合は目標を超える最小値を出力
else:
    print(int(m * n - sum(a)))