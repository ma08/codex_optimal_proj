

import math

def solve(a, b):
    if a > b:
        a, b = b, a
    if a == 1:
        return b + 2
    if a == 2:
        return b + (b % 2) + 2
    s = math.sqrt(a*b)
    if s == int(s):
        return int(2*s)
    k = int(s) + 1
    if k * (k-1) >= a*b:
        return 2*(k-1) + 2
    return 2*k + 2

def main():
    a, b = map(int, input().split())
    print(solve(a, b))

if __name__ == "__main__":
    main()