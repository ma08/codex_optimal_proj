

def main():
    N, M = [int(x) for x in input().split()]
    price_list = [[int(x) for x in input().split()] for i in range(N)]
    price_list.sort()
    total = 0
    for i in range(N):
        if price_list[i][1] <= M:
            total += price_list[i][0] * price_list[i][1]
            M -= price_list[i][1]
        elif price_list[i][1] > M:
            total += price_list[i][0] * M
            M = 0
            break
    print(total)

if __name__ == '__main__':
    main()
