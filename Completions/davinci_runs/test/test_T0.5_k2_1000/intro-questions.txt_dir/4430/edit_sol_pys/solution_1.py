
def solve(n, m, k, a):
    # 先按照箱子排序，从大到小排序
    a.sort(reverse=True)  # 排序
    # 找到第一个箱子放不下的位置，这个位置以后的箱子都不能放下去
    # 所以从前往后排序，找到第一个箱子放不下的位置就是答案
    i = 0  # 记录第一个箱子放不下的位置
    while i < n and a[i] > k:  # 找到第一个箱子放不下的位置
        i += 1  # 更新位置
    if i == n:  # 如果所有箱子都放得下，返回n
        return n  # 返回结果
    # 如果不是所有箱子都放得下，返回第一个箱子放不下的位置
    return i  # 返回结果


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, k, a))
