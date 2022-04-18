

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

    def helper(nums, d, i):
        if i == len(nums):
            return d

        cur = nums[i]

        if cur - 1 in d and cur + 1 in d:
            d[cur] += min(d[cur - 1], d[cur + 1])

        return helper(nums, d, i + 1)

    d = helper(nums, d, 0)

    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
