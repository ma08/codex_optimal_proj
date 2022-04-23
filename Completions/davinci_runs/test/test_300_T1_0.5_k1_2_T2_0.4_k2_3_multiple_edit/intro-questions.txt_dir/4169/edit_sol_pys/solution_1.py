def main():
    N, M = [int(x) for x in input().split()]
    price_list = []
    for i in range(N):
        price_list.append([int(x) for x in input().split()])
    price_list.sort(key=lambda x: x[0])
    total = 0
    while M > 0:
        if price_list[0][1] >= M:
            total += price_list[0][0] * M
            M = 0
        else:
            total += price_list[0][0] * price_list[0][1]
            M -= price_list[0][1]
            price_list.pop(0)
    print(total)

if __name__ == '__main__':
    main()
