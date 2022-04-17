import sys

import math

def main():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))

    days = 0
    for i in range(n):  # i番目の荷物を持っていく
        m -= a[i]  # mは残りの荷物の重さ
        days += 1  # 日数を一日増やす
        if m <= 0:  # mが0以下になったら終了
            print(days)
            sys.exit()

    # mが残っている場合は最後に持っていく荷物の最大値で割れるだけ割って、余りが出る場合は-1
    print(days + math.ceil(m / a[-1])) if m % a[-1] == 0 else print(-1)

if __name__ == "__main__":
    main()
