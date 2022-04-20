

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a = [int(x) for x in input().split()]
    b = a[0]
    for i in range(1, len(a)):
        b = lcm(b, a[i])
    print(b)

if __name__ == '__main__':
    main()
