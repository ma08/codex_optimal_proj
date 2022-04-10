

import sys

def main(n, array):
    # find the gcd of all numbers in the array
    gcd = array[0]
    for i in range(1, len(array)):
        gcd = compute_gcd(gcd, array[i])
    print(count_divisors(gcd))

def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def count_divisors(x):
    count = 0
    i = 1
    while(i * i <= x):
        if(x % i == 0):
            if(x / i == i):
                count += 1
            else:
                count += 2
        i += 1
    return count

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    main(n, array)