

    # n = number of types of items
    # m = number of offers
def main():
    # array of prices of each item
    n, m = map(int, input().split())
    # array of offers
    a = list(map(int, input().split()))
    # for each offer
    offers = []
        # x = first item of the offer
        # y = second item of the offer
        # c = price of the offer
    for i in range(m):
        x, y, c = map(int, input().split())
        offers.append([x, y, c])
    # initially the minimum cost is the sum of the prices of each item

    # for each item
    min_cost = 0
        # add its price to the minimum cost
    for i in range(n):
        min_cost += a[i]
    # for each offer

        # x = first item of the offer
        # y = second item of the offer
        # c = price of the offer
    for offer in offers:
        x, y, c = offer
        # if the sum of the prices of the item is greater than the price of the offer
        if a[x-1] + a[y-1] > c:
            # subtract the sum of the prices of the items from the minimum cost
            min_cost -= a[x-1] + a[y-1]
            min_cost += c

    print(min_cost)


if __name__ == "__main__":
    main()
