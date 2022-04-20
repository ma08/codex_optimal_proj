
def main():
    N, M = [int(x) for x in input().split()]
    price_list = [[int(x) for x in input().split()] for i in range(N)]
    price_list.sort()
    for i in range(N):
        if M == 0:
            break
        if price_list[i][1] >= M:
            total += price_list[i][0] * M
            M = 0
        else:
            total += price_list[i][0] * price_list[i][1]
            M -= price_list[i][1]
    print(total)


def main2():
    N, M = [int(x) for x in input().split()]
    price_list = [[int(x) for x in input().split()] for i in range(N)]
    price_list.sort()
    total = 0
    while M > 0:
        for i in range(N):
            if M == 0:
                break
            if price_list[i][1] >= M:
                total += price_list[i][0] * M
                M = 0
            else:
                total += price_list[i][0] * price_list[i][1]
                M -= price_list[i][1]
    print(total)

if __name__ == '__main__':
    main()
