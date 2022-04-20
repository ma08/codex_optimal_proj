

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # a list of prices
    offers = []
    for i in range(m):
        x, y, c = map(int, input().split())
        offers.append([x-1, y-1, c])  # subtract 1 since we use 0-based index

    min_cost = 0
    for i in range(n):
        min_cost += a[i]

    for offer in offers:
        x, y, c = offer[0], offer[1], offer[2]
        if a[x] + a[y] > c:
            min_cost -= a[x] + a[y]
            min_cost += c

    print(min_cost)


if __name__ == "__main__":
    main()
