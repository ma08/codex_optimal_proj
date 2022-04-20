
def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a, b = map(int, input().split())
    print(lcm(a, b))

if __name__ == '__main__':
    main()