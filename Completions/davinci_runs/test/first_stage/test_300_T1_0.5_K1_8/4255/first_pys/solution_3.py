

import math

def main():
    ab, bc, ca = map(int, input().split())
    s = (ab + bc + ca) / 2
    area = math.sqrt(s * (s - ab) * (s - bc) * (s - ca))
    print(int(area))

if __name__ == '__main__':
    main()