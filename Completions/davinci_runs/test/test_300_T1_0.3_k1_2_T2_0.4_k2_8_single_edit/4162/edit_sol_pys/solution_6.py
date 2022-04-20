
import sys


def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    # 全てのa_iについて、a_iの倍数を求める
    # それぞれのa_iの倍数で、f(m)が最大となるmを求める
    # その中で最大のf(m)を出力する
    max_f = 0
    for i in range(N):
        m = A[i]
        f = m
        while f > max_f:
            for j in range(N):
                if j == i:
                    continue
                f += m % A[j]
            max_f = max(max_f, f)
            m += A[i]
            f = m

    print(max_f)


if __name__ == '__main__':
    main()
