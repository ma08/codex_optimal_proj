# -*- coding: utf-8 -*-

def main():
    n, m = [int(i) for i in input().split()]  # n为应用个数，m为手机内存。
    a = [int(i) for i in input().split()]  # 应用占用内存。
    a.sort()  # 升序排序。
    if a[0] > m:  # 如果最小的应用内存大于手机内存，则不能安装任何应用。
        print(-1)
        return
    i = 0  # 应用索引。
    days = 0  # 安装应用天数。
    while m > 0:  # 如果手机内存大于0。
        m -= a[i]  # 手机内存减去当前应用占用内存。
        i += 1  # 应用索引加1。
        days += 1  # 安装应用天数加1。
        if i == n:  # 如果应用索引等于应用个数，则重新开始。
            i = 0
    print(days)  # 输出安装应用天数。


if __name__ == "__main__":
    main()
