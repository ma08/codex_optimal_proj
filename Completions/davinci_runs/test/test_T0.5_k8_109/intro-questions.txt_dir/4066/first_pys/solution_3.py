

import math

lst = [2, 4, 8, 3, 6]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    n = int(input())
    lst = list(map(int, input().split()))
    min_lcm = 10 ** 7
    ans = (1, 2)
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if lcm(lst[i - 1], lst[j - 1]) < min_lcm:
                min_lcm = lcm(lst[i - 1], lst[j - 1])
                ans = (i, j)
    print(ans[0], ans[1])

if __name__ == "__main__":
    main()