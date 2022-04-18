

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if c % gcd(a, b) == 0:
        print("YES")
    else:
        print("NO")
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()
