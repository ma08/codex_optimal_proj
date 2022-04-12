

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    m, sigma = map(int, sys.stdin.readline().split())

    # let x = y, then 2x + y = sigma, 3x = sigma, x = sigma/3
    # x + y <= m, 2x <= m, x <= m/2
    # x >= 1, y >= 1
    # so we have sigma/3 >= x >= m/2
    # we want the max of 3x^2 - 2ax + a, which is the rent
    # derivative is 6x - 2a
    # 6x - 2a = 0, 3x = a, x = a/3
    # 3x^2 - 2ax + a = 3(a/3)^2 - 2a(a/3) + a = a^2/3 - a^2/3 + a = a
    # so max rent is a

    print(a)

if __name__ == "__main__":
    main()
