# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))


# 入力
N = int(input())
A = list(map(int, input().split()))

# 最大公約数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# 初期値
gcd_max = 0

# 全組み合わせで最大公約数を求める
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
