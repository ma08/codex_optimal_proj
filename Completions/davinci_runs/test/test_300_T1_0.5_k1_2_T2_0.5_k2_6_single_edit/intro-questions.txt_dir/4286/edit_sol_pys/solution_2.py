

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # a[i]: cost of i-th item
    offers = []
    for i in range(m):
        x, y, c = map(int, input().split())  # x, y: item number, c: cost of the offer
        offers.append([x, y, c])  # offers[i]: the i-th offer

    min_cost = 0
    for i in range(n):
        min_cost += a[i]  # initial minimum cost

    for offer in offers:
        x, y, c = offer  # offer[i]: the i-th offer
        if a[x-1] + a[y-1] > c:  # if the offer is cheaper than buying the two items separately
            min_cost -= a[x-1] + a[y-1]  # remove the cost of the two items from the minimum cost
            min_cost += c  # add the cost of the offer to the minimum cost

    print(min_cost)


if __name__ == "__main__":
    main()
