

def gcd(a, b):
    return b == 0 and a or gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    print(reduce(lcm, map(int, input().split())))

if __name__ == '__main__':
    main()
