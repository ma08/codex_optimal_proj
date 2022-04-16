# coding=utf-8


def solve(n, m, k, a):
    # 先按照箱子排序
    a.sort(reverse=True)
    # 找到第一个箱子放不下的位置
    i = 0
    while i < n:
        if a[i] > k:
            break
        i += 1
    if i == n:
        return n
    # 找到第一个箱子放不下的位置，这个位置以后的箱子都不能放下
    # 所以从前往后排序，找到第一个箱子放不下的位置就是答案
    a.sort()
    i = 0
    while i < n:
        if a[i] > k:
            break
        i += 1
    return i


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, k, a))
