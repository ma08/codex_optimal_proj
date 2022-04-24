
def main():
    n = int(input())
    nums = [int(i) for i in input().split()]

    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1

    sorted_nums = sorted(d.keys())

    def helper(sorted_nums, d, i):
        if i == len(sorted_nums):
            return

        cur = sorted_nums[i]
        if cur - 1 in d and cur + 1 in d:
            d[cur] = d[cur - 1] + d[cur + 1]
        helper(sorted_nums, d, i + 1)

    d = helper(nums, d, 0)

    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in sorted_nums if d[i] == res]))

if __name__ == '__main__':
    main()
