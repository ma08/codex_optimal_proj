

def main():
    n = int(input())
    x = [int(i) for i in input().split()]

    d = {}
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    nums = sorted(d.keys())

    def helper(nums, d, i, res):
        if i == len(nums):
            return res

        cur = nums[i]

        if cur - 1 in d:
            d[cur] += d[cur - 1]
        if cur + 1 in d:
            d[cur] += d[cur + 1]

        return helper(nums, d, i + 1, max(res, d[cur]))

    res = helper(nums, d, 0, 0)

    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
