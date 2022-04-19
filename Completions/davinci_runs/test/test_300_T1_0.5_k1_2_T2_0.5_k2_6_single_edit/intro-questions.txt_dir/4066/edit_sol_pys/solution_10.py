

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    

if __name__ == '__main__':
    main()
