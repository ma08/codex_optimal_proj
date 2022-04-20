

import math

def main():
    a, b = [int(x) for x in input().split()]
    if a == b:
        print(4*a)
    else:
        c = math.gcd(a, b)
        print(2*(a+b)//c)

if __name__ == '__main__':
    main()