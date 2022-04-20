import math

input = sys.stdin.readline
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    lcm = a[0] * a[1] // math.gcd(a[0], a[1])
    for i in range(2, n):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    print(lcm)

if __name__ == '__main__':
    main()
