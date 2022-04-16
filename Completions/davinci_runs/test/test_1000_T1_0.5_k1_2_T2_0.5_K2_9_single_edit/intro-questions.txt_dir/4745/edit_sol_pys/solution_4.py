

def main():
    """find the maximum number of items that can be marked as part of the special offer."""
    n, x = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    total = 0
    count = 0
    for i in prices:
        if i + total > x:
            break
        total += i
        count += 1
    print(count)

if __name__ == '__main__':
    main()
