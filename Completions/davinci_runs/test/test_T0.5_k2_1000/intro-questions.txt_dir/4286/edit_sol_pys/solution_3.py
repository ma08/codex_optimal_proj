
def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))[:n]
    offers = [list(map(int, input().split())) for i in range(m)]

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
