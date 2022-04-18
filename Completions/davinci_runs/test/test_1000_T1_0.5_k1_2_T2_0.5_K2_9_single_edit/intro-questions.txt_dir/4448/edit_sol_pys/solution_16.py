

def main():
    n, m = [int(x) for x in input().split()] # n = number of items, m = number of offers
    k = [int(x) for x in input().split()] # k = list of items
    offers = []
    for _ in range(m): # creates a list of lists with offers
        offers.append([int(x) for x in input().split()])
    days = [0] * (n + 1) # creates a list of zeroes
    for day, kind in offers:
        days[kind] = max(days[kind], day) # replaces the 0 with the day of the offer
    result = 0
    for kind, day in enumerate(days):
        if k[kind] > 0: # if there are any items of that kind
            result = max(result, day + (k[kind] - 1) * 2) # finds the maximum number of days
    print(result)

if __name__ == '__main__':
    main()
