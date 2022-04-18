
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if a[-1] >= m:  # m개 이상의 사과를 수집하려면 하루만에 가능함
        print(1)
        return

    days = 0
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0:  # 사과를 다 수집했으면 종료
            print(days)
            return

    if m % a[-1] == 0:
        print(days + math.ceil(m / a[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
