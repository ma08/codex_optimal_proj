

def main():
    n = int(input())
    x = [int(i) for i in input().split()]

    d = {}
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    nums = sorted(list(d.keys()))

    def helper(nums, d, i=0):
        if i == len(nums):
            return d

        if nums[i] - 1 in d:
            d[nums[i]] += d[nums[i] - 1]
        if nums[i] + 1 in d:
            d[nums[i]] += d[nums[i] + 1]

        return helper(nums, d, i + 1)

    d = helper(nums, d)

    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
