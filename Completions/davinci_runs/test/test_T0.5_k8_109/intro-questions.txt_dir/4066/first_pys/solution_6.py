

import sys

def lcm(x, y):
    return (x * y) // gcd(x, y)

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    min_lcm = float('inf')
    min_i = min_j = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            lcm_ij = lcm(arr[i], arr[j])
            if lcm_ij < min_lcm:
                min_lcm = lcm_ij
                min_i = i + 1
                min_j = j + 1
    print(min_i, min_j)

if __name__ == '__main__':
    main()