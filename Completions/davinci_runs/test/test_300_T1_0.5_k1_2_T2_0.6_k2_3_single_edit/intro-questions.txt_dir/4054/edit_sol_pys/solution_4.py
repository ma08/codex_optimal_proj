def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    b = [int(x) for x in input().split()]
    c = b[0]
    for i in range(1, len(b)):
        c = lcm(c, b[i])
    print(b)

if __name__ == '__main__':
    main()
