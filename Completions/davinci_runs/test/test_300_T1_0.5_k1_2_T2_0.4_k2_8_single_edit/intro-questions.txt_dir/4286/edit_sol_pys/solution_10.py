

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # a[i] = cost of ith item
    offers = []
    for i in range(m):
        x, y, c = map(int, input().split())
        offers.append([x, y, c])

    min_cost = sum(a)

    for offer in offers:
        x, y, c = offer
        if a[x-1] + a[y-1] > c:
            min_cost -= a[x-1] + a[y-1]
            min_cost += c

    print(min_cost)


if __name__ == "__main__":
    main()
