

# 入力部
N = int(input())
A = list(map(int, input().split()))

# 最大公約数を求める関数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# 最大公約数
gcd_max = 0

for i in range(N):
    for j in range(N):
        # 自分自身と比較しない
        if i != j:
            # 最大公約数
            gcd_tmp = gcd(A[i], A[j])
            # 更新
            if gcd_max < gcd_tmp:
                gcd_max = gcd_tmp

# 出力部
print(gcd_max)
