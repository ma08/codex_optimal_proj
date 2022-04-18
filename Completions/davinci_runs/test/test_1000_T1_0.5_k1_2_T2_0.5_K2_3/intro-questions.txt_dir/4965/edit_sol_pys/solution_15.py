

def main():
    n = int(input())  # n个数
    t = list(map(int, input().split()))  # 输入n个数
    t.sort()  # 排序
    if n % 2 == 0:  # 如果n为偶数
        for i in range(n // 2):  # 从0到n/2
            t[i], t[n - 1 - i] = t[n - 1 - i], t[i]  # 把t[i]和t[n-1-i]交换
    else:  # 如果n为奇数
        for i in range(n // 2):  # 从0到n/2
            t[i], t[n - 1 - i] = t[n - 1 - i], t[i]  # 把t[i]和t[n-1-i]交换
    print(*t)  # 输出


if __name__ == "__main__":
    main()
