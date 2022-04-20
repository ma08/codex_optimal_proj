

def main():
    n, m = map(int, input().split())  # n: number of items, m: number of offers
    a = list(map(int, input().split()))  # a: price of each item
    offers = []
    for i in range(m):
        x, y, c = map(int, input().split())  # x, y: items in offer, c: discount
        offers.append([x, y, c])

    min_cost = 0
    for i in range(n):
        min_cost += a[i]

    for offer in offers:
        x, y, c = offer
        if a[x-1] + a[y-1] > c:
            min_cost -= a[x-1] + a[y-1]
            min_cost += c

    print(min_cost)


if __name__ == "__main__":
    main()
