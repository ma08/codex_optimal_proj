
import math

def lcm(a,b):
    return a*b//math.gcd(a,b)

if __name__ == "__main__":
    a, b = [int(i) for i in input().split()]
    print(lcm(a, b))

if __name__ == '__main__':
    main()
