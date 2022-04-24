

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for i in range(m):
        x, y, c = map(int, input().split())
        offers.append([x, y, c])

    min_price = 0
    for i in range(n):
        min_price += a[i]

    for offer in offers:
        x, y, c = offer
        if a[x-1] + a[y-1] > c:
            min_price -= a[x-1] + a[y-1]
            min_price += c

    print(min_price)


if __name__ == "__main__":
    main()
