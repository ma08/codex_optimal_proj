
def main():
    N, M = [int(x) for x in input().split()]
    price_list = []
    for i in range(N):
        price_list.append([int(x) for x in input().split()])  # 读取数据
    price_list.sort()
    total = 0
    while M > 0:  # 如果还有需求
        if price_list[0][1] >= M:  # 如果当前供应量大于需求量
            total += price_list[0][0] * M  # 则当前供应商提供全部
            M = 0
        else:
            total += price_list[0][0] * price_list[0][1]
            M -= price_list[0][1]
            price_list.pop(0)
    print(total)

if __name__ == '__main__':
    main()
