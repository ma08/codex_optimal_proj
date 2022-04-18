

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    m, sigma = map(int, sys.stdin.readline().split())

    # let x = y, then 2x + y >= sigma, x >= sigma/2
    # x + y <= m, x <= m/2
    # x >= 1
    # so we have sigma/2 <= x <= m/2
    # we want the max of xy - ax - by
    # derivative is y - a
    # y - a = 0, y = a, x = m - a
    # xy - ax - by = (m-a)(a) - a(m-a) - a(m-a) = -a^2 + m * a - a^2 + a^2 = m * a - a^2
    # so max rent is m * a - a^2
    if (a * 2 > sigma):
        print("0")
        return
    if (m * a - a * a < 0):
        print("0")
        return
    print(m * a - a * a)

if __name__ == "__main__":
    main()
