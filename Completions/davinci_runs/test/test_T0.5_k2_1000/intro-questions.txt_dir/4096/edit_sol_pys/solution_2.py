
import math
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = sorted(list(map(int, sys.stdin.readline().split())))

    if a[-1] >= m:
        sys.stdout.write(str(1))
        return

    days = 0
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0:
            sys.stdout.write(str(days))
            return

    if m % a[-1] == 0:
        sys.stdout.write(str(days + math.ceil(m / a[-1])))
    else:
        sys.stdout.write(str(-1))


if __name__ == "__main__":
    main()
