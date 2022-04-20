

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b, k = map(int, input().split())
    l = lcm(a, b)
    c = 0
    for i in range(1, l + 1):
        if l % i == 0:
            c += 1
            if c == k:
                print(i)
                break

if __name__ == '__main__':
    main()