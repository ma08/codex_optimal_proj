import sys


def main():
    # N, M = [int(x) for x in input().split()]
    # price_list = []
    # for i in range(N):
    #     price_list.append([int(x) for x in input().split()])
    # price_list.sort()
    # total = 0
    # while M > 0:
    #     if price_list[0][1] >= M:
    #         total += price_list[0][0] * M
    #         M = 0
    #     else:
    #         total += price_list[0][0] * price_list[0][1]
    #         M -= price_list[0][1]
    #         price_list.pop(0)
    # print(total)
    N, M = map(int, input().split())
    price = []
    for i in range(N):
        price.append(list(map(int, input().split())))
    price.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if M <= price[i][1]:
            ans += price[i][0] * M
            break
        else:
            ans += price[i][0] * price[i][1]
            M -= price[i][1]
    print(ans)

if __name__ == '__main__':
    main()
