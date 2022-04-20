

from fractions import gcd
from functools import reduce

def number_of_common_divisors(numbers):
    return reduce(gcd, numbers)

def main():
    _ = int(input())
    numbers = list(map(int, input().split()))
    print(number_of_common_divisors(numbers))

if __name__ == "__main__":
    main()