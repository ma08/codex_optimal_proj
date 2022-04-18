
def main():
    n = int(input())
    x = [int(i) for i in input().split()]  # 输入数组

    d = {}  # 存放数组中每个元素出现的次数
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    nums = sorted(d.keys())  # 数组中元素排序

    def helper(nums, d, i):  # 递归
        if i == len(nums):
            return d

        cur = nums[i]  # 当前元素

        if cur - 1 in d:  # 如果当前元素的前一个元素在字典中，则当前元素的出现次数增加前一个元素的出现次数
            d[cur] += d[cur - 1]
        if cur + 1 in d:
            d[cur] += d[cur + 1]

        return helper(nums, d, i + 1)

    d = helper(nums, d, 0)

    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
