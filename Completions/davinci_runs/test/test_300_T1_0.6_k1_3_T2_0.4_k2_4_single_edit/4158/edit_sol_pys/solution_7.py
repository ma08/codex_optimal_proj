

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

    def helper(nums, d, j):
        if j == len(nums):
            return d

        cur = nums[j]

        if cur - 1 in d:
            d[cur] += d[cur - 1]
        if cur + 1 in d:
            d[cur] += d[cur + 1]

        return helper(nums, d, j + 1)

    d = helper(nums, d, 0)

    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
