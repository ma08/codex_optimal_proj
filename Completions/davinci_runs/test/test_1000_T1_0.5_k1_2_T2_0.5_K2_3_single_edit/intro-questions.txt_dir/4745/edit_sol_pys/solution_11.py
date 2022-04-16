

def main(n, x, prices):
    """find the maximum number of items that can be marked as part of the special offer
    n: number of items
    x: maximum price
    prices: list of prices of items
    """
    # n, x = map(int, input().split())
    # prices = list(map(int, input().split()))
    # prices.sort()
    # total = 0
    # count = 0
    # for i in prices:
    #     if i + total > x:
    #         break
    #     total += i
    #     count += 1
    # print(count)
    prices.sort(reverse=True)
    total = sum(prices)
    count = len(prices)
    while total > x:
        total -= prices.pop()
        count -= 1
    return count


if __name__ == '__main__':
    print(main(3, 7, [1, 2, 3]))
