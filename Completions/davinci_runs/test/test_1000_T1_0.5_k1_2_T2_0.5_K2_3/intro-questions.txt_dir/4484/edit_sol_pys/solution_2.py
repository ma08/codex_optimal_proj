

def main():
    n, m = map(int, input().split())
    MOD = 10 ** 9 + 7

    # 全て犬にする場合
    all_dogs_case = 1
    for i in range(n):
        all_dogs_case *= (m + i)
        all_dogs_case %= MOD

    # 全て猿にする場合
    all_monkeys_case = 1
    for i in range(m):
        all_monkeys_case *= (n + i)
        all_monkeys_case %= MOD

    # それ以外の場合
    # 犬に猿を入れる場合
    # 猿に犬を入れる場合
    # 上記2つの場合を足す
    # なぜなら、猿に犬を入れた場合とその逆の場合は同じになるから
    # 犬に猿を入れていく場合
    # 犬が1匹の時
    # 猿が1匹の時
    # 犬が2匹の時
    # 猿が2匹の時
    # ...
    # 犬がn匹の時
    # 猿がm匹の時
    # これを繰り返していく
    # 猿に犬を入れていく場合
    # 猿が1匹の時
    # 犬が1匹の時
    # 猿が2匹の時
    # 犬が2匹の時
    # ...
    # 猿がm匹の時
    # 犬がn匹の時
    # これを繰り返していく
    others_case = 0
    for i in range(1, n + 1):
        # i匹の犬にj匹の猿を入れる場合
        for j in range(1, m + 1):
            # 犬に猿を入れる
            # 犬の数がi匹なので、猿はi-1匹まで入れられる
            # 猿の数がj匹なので、犬はj-1匹まで入れられる
            # (i-1)+(j-1)C(j-1)
            others_case += (i - 1 + j - 1) * nCr(i - 1 + j - 1, i - 1)
            others_case %= MOD

            # 猿に犬を入れる
            # 猿の数がj匹なので、犬はj-1匹まで入れられる
            # 犬の数がi匹なので、猿はi-1匹まで入れられる
            # (j-1)+(i-1)C(i-1)
            others_case += (j - 1 + i - 1) * nCr(j - 1 + i - 1, j - 1)
            others_case %= MOD

    print((all_dogs_case + all_monkeys_case + others_case) % MOD)

def nCr(n, r):
    """
    nCrを求める
    """
    MOD = 10 ** 9 + 7
    # nCr = n! / (n-r)!r!
    # n!を求める
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial *= i
        n_factorial %= MOD
    # (n-r)!r!を求める
    n_r_factorial = 1
    for i in range(1, n - r + 1):
        n_r_factorial *= i
        n_r_factorial %= MOD
    r_factorial = 1
    for i in range(1, r + 1):
        r_factorial *= i
        r_factorial %= MOD
    n_r_factorial *= r_factorial
    n_r_factorial %= MOD
    # (n-r)!r!の逆元を求める
    n_r_factorial_inv = pow(n_r_factorial, MOD - 2, MOD)
    # nCrを求める
    nCr = n_factorial * n_r_factorial_inv % MOD
    return nCr

if __name__ == '__main__':
    main()
