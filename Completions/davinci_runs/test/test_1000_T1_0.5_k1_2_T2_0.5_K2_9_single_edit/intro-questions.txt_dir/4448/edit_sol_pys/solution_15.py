
def main():
    n, m = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]
    offers = []
    for _ in range(m):
        day, kind = [int(x) for x in input().split()]
        offers.append((day, kind))
    days = [0] * (n + 1)
    for offer in offers:
        day, kind = offer
        days[kind] = max(days[kind], day)
    result = 0
    for kind, day in enumerate(days):
        if k[kind] > 0:
            result = max(result, day + (k[kind] - 1) * 2)
    print(result)

if __name__ == '__main__':
    main()
