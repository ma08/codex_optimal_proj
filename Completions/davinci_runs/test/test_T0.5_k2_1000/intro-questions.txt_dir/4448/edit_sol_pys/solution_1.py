

def main():
    n, m = [int(x) for x in input().split()]  # n - number of days, m - number of offers, k - number of offers for each day
    offers = []
    for _ in range(m):
        offers.append([int(x) for x in input().split()])  # offers - list of offers (day, kind)
    days = [0] * (n + 1)
    for day, kind in offers:
        days[kind] = max(days[kind], day)
    result = 0
    for kind, day in enumerate(days[1:], 1):
        if k[kind - 1] > 0:
            result = max(result, day + (k[kind - 1] - 1) * 2)
    print(result)

if __name__ == '__main__':
    main()
