

# SOLUTIONS

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

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
