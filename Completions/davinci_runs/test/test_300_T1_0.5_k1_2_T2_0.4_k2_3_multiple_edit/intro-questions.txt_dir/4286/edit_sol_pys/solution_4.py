
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # a[i] is the price of the i-th item
    offers = []
    for i in range(m):
        x, y, c = map(int, input().split())
        offers.append([x, y, c])  # x, y are the indices of the items and c is the price of the offer

    min_cost = 0
    for i in range(n):
        min_cost += a[i]

    for offer in offers:
        x, y, c = offer
        if a[x-1] + a[y-1] > c:
            min_cost -= a[x-1] + a[y-1]
            min_cost += c

    print(int(min_cost))


if __name__ == "__main__":
    main()
