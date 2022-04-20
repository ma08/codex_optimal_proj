


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for i in a[1:]:
        g = gcd(g, i)
    cnt = 0
    for i in range(1, int(g ** 0.5) + 1):
        if g % i == 0:
            cnt += 1
    if g ** 0.5 == int(g ** 0.5):
        cnt -= 1
    print(cnt * 2 + 1)


if __name__ == '__main__':
    main()