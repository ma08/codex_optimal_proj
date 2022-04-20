

import math

def main():
    x, k, d = map(int, input().split())
    if k <= abs(x) // d:
        print(abs(x) - k * d)
    else:
        print(abs(x - (k - abs(x) // d) * d * math.copysign(1, x)))

if __name__ == '__main__':
    main()