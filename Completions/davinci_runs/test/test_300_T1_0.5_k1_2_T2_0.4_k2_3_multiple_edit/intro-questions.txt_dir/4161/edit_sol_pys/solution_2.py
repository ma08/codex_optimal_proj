

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    k = int(input())

    ans = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for l in range(1, k + 1):
                ans += gcd(i, j)
                ans += gcd(j, l)
                ans += gcd(l, i)
                ans += gcd(gcd(i, j), l)
    print(ans)

if __name__ == '__main__':
    main()
