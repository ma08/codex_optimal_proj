
from collections import defaultdict

def happiness(x, n):
    d = defaultdict(int)  # 使用字典记录每种硬币的数量
    for i in range(len(n)):  # 遍历硬币种类
        d[n[i]] = x // n[i]  # 计算每种硬币的数量
        x %= n[i]  # 计算剩余的金额
    return 1000 * d[500] + 5 * d[5]  # 计算幸福感


if __name__ == '__main__':
    x = int(input())
    n = [500, 100, 50, 10, 5, 1]
    print(happiness(x, n))
