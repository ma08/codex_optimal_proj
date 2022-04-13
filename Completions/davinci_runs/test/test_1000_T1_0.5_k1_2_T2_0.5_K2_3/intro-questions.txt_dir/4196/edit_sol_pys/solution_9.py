

# 最大公約数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# 入力
N = int(input())
A = list(map(int, input().split()))

def main():
    # 初期値
    gcd_max = 0

    # 全組み合わせ(重複なし)
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

if __name__ == "__main__":
    main()
