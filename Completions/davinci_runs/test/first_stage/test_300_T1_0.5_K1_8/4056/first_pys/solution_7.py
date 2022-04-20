

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    c = 0
    for i in range(1, int(g ** 0.5) + 1):
        if g % i == 0:
            c += 1
            if i * i != g:
                c += 1
    print(c)

if __name__ == "__main__":
    main()