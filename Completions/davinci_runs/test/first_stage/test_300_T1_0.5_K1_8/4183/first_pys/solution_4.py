

def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = a[0]
    for i in range(n-1):
        ans = lcm(ans, a[i+1])
    print(ans)

if __name__ == '__main__':
    main()