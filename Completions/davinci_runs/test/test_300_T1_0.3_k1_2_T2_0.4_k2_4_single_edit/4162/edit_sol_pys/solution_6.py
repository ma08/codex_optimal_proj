
import math
import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # 全てのa_iについて、a_iの倍数を求める
    # それぞれのa_iの倍数で、f(m)が最大となるmを求める
    # その中で最大のf(m)を出力する
    max_f = 0
    for i in range(n):  # a_iについて
        m = a[i]  # a_iの倍数を求める
        f = m  # f(m)を初期化
        while f > max_f:  # f(m)が最大となるmを求める
            for j in range(n):  # それぞれのa_iの倍数で
                if j == i:  # a_i自身は除く
                    continue  # a_iの倍数で
                f += m % a[j]  # f(m)を求める
            max_f = max(max_f, f)  # その中で最大のf(m)を出力する
            m += a[i]  # a_iの倍数を求める
            f = m  # f(m)を初期化

    print(max_f)


if __name__ == '__main__':
    main()
