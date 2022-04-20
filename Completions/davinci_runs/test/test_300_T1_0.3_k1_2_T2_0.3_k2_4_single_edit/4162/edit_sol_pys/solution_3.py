
import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # 全てのa_iについて、a_iの倍数を求める
    # それぞれのa_iの倍数で、f(m)が最大となるmを求める
    # その中で最大のf(m)を出力する
    max_f = 0
    for i in range(n):
        m = a[i]
        while True:
            f = m
            for j in range(n):
                if j == i:
                    continue
                f += m % a[j]
            max_f = max(max_f, f)
            if f <= max_f:
                break
            m += a[i]
            f = m

    print(max_f)


if __name__ == '__main__':
    main()
