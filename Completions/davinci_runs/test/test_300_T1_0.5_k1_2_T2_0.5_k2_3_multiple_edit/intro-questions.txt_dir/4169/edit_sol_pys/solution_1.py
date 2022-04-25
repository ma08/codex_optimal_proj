
def main():
    n, m = [int(x) for x in input().split()]
    price_list = sorted([[int(x) for x in input().split()] for i in range(n)], key=lambda x: x[0])
    total = 0
    while m > 0:
        if price_list[0][1] >= m:
            total += price_list[0][0] * m
            m = 0
        else:
            total += price_list[0][0] * price_list[0][1]
            m -= price_list[0][1]
            price_list.pop(0)
    print(total)

if __name__ == '__main__':
    main()
