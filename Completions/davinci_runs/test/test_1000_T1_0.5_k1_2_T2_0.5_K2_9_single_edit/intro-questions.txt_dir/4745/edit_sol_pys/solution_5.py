

def main():
    n, x = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    total = 0
    count = 0
    for price in prices:
        if price + total > x:
            break
        total += price
        count += 1
    print(count)

if __name__ == '__main__':
    main()
