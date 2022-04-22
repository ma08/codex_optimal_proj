

def main():
    N, M = [int(x) for x in input().split()]
    price_list = []  # 定义一个列表用来存放每个种类的价格和数量，price_list[i][0]为第i种类的价格，price_list[i][1]为第i种类的数量
    for i in range(N):
        price_list.append([int(x) for x in input().split()])  # 将输入的价格和数量存放到列表中
    price_list.sort(key=lambda x: x[0])  # 对列表按第一个元素进行排序
    total = 0
    while M > 0:  # 如果还有需求
        if price_list[0][1] >= M:  # 如果第一个种类的数量大于需求
            total += price_list[0][0] * M
            M = 0  # 需求清零
        else:
            total += price_list[0][0] * price_list[0][1]  # 如果第一个种类的数量小于需求
            M -= price_list[0][1]  # 需求减去第一个种类的数量
            price_list.pop(0)  # 删除第一个种类
    print(total)

if __name__ == '__main__':
    main()
