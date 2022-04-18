

    # TODO: implement
def main():
    n, m = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]
    offers = []
    for _ in range(m):
        offers.append([int(x) for x in input().split()])
    days = [0] * (n + 1)
    for day, kind in offers:
        days[kind] = max(days[kind], day)
    result = 0
    for kind, day in enumerate(days):
        if k[kind] > 0:
            result = max(result, day + (k[kind] - 1) * 2)
    print(result)

if __name__ == '__main__':
    main()
