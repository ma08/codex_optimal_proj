

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    a, b, c, d = map(int, input().split())
    l = lcm(c, d)
    print(b - a - (b // c - (a - 1) // c) - (b // d - (a - 1) // d) + b // l - (a - 1) // l + 1)

if __name__ == '__main__':
    main()