

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    A, B, C, D = map(int, input().split())
    # A以上B以下の範囲でCまたはDで割り切れる数を求める
    # CまたはDで割り切れる数は、CとDの最小公倍数で割り切れる数のみ
    l = lcm(C, D)
    c_cnt = math.ceil((B + 1 - C) / C)
    d_cnt = math.ceil((B + 1 - D) / D)
    l_cnt = math.ceil((B + 1 - l) / l)
    # print(c_cnt, d_cnt, l_cnt)
    c_cnt -= math.ceil((A - C) / C)
    d_cnt -= math.ceil((A - D) / D)
    l_cnt -= math.ceil((A - l) / l)
    # print(c_cnt, d_cnt, l_cnt)
    print(B - A + 1 - (c_cnt + d_cnt - l_cnt))

if __name__ == '__main__':
    main()