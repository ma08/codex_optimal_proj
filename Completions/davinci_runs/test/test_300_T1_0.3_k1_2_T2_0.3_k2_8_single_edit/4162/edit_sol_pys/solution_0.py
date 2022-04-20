import sys

def main():
    n = int(input())
    a = list(map(int, input().split())
    print(lcm(a))

def lcm(a):
    l = a[0]
    for i in range(1, len(a)):
        l = l * a[i] // gcd(l, a[i])
    return l

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

if __name__ == '__main__':
    main()
