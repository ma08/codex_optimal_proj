

import math


def main():
    a, b = map(int, input().split())  # read a list of integers, 2 in this case

    print(a * b // math.gcd(a, b))

if __name__ == '__main__':
    main()
