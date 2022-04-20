
def main():
    n = int(input())
    x = [int(i) for i in input().split()]

    d = {}
    for i in x:
        d[i] = d.get(i, 0) + 1

    nums = sorted(d.keys())

    def helper(d, i):
        if i == len(nums) - 1:
            return

        cur = nums[i]

        if cur - 1 in d and cur + 1 in d:
            d[cur] += d[cur - 1] + d[cur + 1]
        elif cur - 1 in d:
            d[cur] += d[cur - 1]
        elif cur + 1 in d:
            d[cur] += d[cur + 1]

        return helper(d, i + 1)

    helper(d, 0)

    res = max(d.values())
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
