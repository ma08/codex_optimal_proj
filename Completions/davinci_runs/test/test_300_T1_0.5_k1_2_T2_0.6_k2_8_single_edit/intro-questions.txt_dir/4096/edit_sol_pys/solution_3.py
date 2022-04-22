
import math
import sys

def main():
    n, m = map(int, input().split())  # n: 生徒数, m: 宿題の重要度の総和
    a = list(map(int, input().split()))  # 各生徒の宿題の重要度
    a.sort()  # 宿題の重要度を昇順にソート
    # 宿題の最大値が宿題の重要度の総和より大きい場合

        return

    # 宿題の重要度の総和を最も重要度の低い生徒が持っている宿題の重要度で割った商が回答
    if m % a[0] == 0:
        print(m // a[0])
    if a[-1] >= m:
        print(1)
        # 宿題の重要度の総和から宿題の重要度を引いていく
        return
        # 生徒数を1増やしていく

    days = 0
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0:
            print(days)
            return

    if m % a[-1] == 0:
        print(days + math.ceil(m / a[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
