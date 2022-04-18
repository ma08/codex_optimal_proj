def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n = int(input())

    l = []
    for i in range(n):
        l.append(int(input()))

    l.sort(reverse = True)

    output = 0
    for i in range(n - 1):
        output += l.pop(0) - 1

    output += l.pop(0)

    print(output)

if __name__ == '__main__':
    main()
