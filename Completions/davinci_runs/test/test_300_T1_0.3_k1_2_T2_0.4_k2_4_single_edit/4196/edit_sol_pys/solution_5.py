
import math

import math

def gcd(a, b):
    return math.gcd(a, b)

def gcd_list(numbers):
    return reduce(gcd, numbers)

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(gcd_list(numbers))

if __name__ == '__main__':
    main()
