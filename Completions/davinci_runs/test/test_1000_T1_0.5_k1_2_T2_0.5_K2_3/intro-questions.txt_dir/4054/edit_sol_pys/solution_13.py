
#SOLUTION FOR LEAST COMMON MULTIPLE

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b = [int(x) for x in input().split()]
    print(lcm(a, b))

if __name__ == '__main__':
    main()
