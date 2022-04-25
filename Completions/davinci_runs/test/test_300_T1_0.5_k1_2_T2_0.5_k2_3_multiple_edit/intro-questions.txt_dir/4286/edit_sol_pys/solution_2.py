
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []  # list of offers
    for i in range(m):
        x, y, c = map(int, input().split())
        offers.append([x, y, c])

    min_cost = 0
    for i in range(n):
        min_cost += a[i]

    for offer in offers:  # iterate through all offers
        x, y, c = offer
        if a[x-1] + a[y-1] > c:  # if cost of buying 2 items is more than cost of buying 1 item
            min_cost -= a[x-1] + a[y-1]
            min_cost += c

    print(min_cost)  # print the minimum cost


if __name__ == "__main__":
    main()
