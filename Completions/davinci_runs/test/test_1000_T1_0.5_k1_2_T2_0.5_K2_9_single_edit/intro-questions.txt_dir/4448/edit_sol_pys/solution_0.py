

def main():
    n, m = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]
    offers = []
    for _ in range(m):
        offers.append([int(x) - 1 for x in input().split()])
    days = [0] * (n + 1)
    for day, kind in offers:
        days[kind] = max(days[kind], day)
    result = 0
    for kind, num in enumerate(k):
        if num > 0:
            result = max(result, days[kind] + (num - 1) * 2)
    print(result)

if __name__ == '__main__':
    main()
