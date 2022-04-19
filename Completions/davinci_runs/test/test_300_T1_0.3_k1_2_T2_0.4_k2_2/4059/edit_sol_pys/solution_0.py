

import math
import sys


def main():
    N = int(input())
    count = 0
    for a in range(1, int(math.sqrt(N)) + 1):  # aを固定
        for b in range(1, int(math.sqrt(N)) + 1):  # bを固定
            if a * b + b > N:  # a*b+b>Nならばそれ以上は探索する必要がない
                break  # ループを抜ける
            if (N - b) % a == 0:  # a*b+b<=Nかつ(N-b)%a==0ならば解が存在
                count += 1  # 解の個数をカウント
    print(count)


if __name__ == '__main__':
    main()
