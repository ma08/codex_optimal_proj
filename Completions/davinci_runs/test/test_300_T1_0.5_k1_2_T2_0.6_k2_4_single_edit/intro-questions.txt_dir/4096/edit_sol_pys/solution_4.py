

import math
import sys

    # n: 果物の数, m: 必要な果物の重さ
def main():
    # a: 果物の一覧
    n, m = map(int, input().split())
    # aを昇順にソート
    a = list(map(int, input().split()))
    # aの最大値がm以上なら、最初に選んだ果物でmを作れるので、答えは1
    a.sort()

    if a[-1] >= m:
        print(1)
        return

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
