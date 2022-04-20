

# 入力
N = int(input())
A = list(map(int, input().split()))

# 初期値
lcm_min = 0

# 全組み合わせ
for i in range(N):
    for j in range(N):
        # 自分自身と比較しない
        if i != j:
            # 最大公約数
            gcd_tmp = gcd(A[i], A[j])
            # 更新
            if gcd_max < gcd_tmp:
                gcd_max = gcd_tmp

# 出力
print(gcd_max)
