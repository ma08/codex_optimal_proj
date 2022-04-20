

import math

def main():
    AB, BC, CA = map(int, input().split())
    s = (AB + BC + CA) / 2
    area = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))
    print(int(area))

if __name__ == '__main__':
    main()