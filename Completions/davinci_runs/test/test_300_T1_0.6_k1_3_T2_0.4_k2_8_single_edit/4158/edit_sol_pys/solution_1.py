
def main():
    n = int(input())
    x = [int(i) for i in input().split()][:n]

    d = {}
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    nums = sorted(d.keys())

    def helper(nums, d, i, n):
        if i == n:
            return

        cur = nums[i]

        if cur - 1 in d and cur + 1 in d:
            d[cur] += d[cur - 1] + d[cur + 1]
        elif cur - 1 in d:
            d[cur] += d[cur - 1]
        elif cur + 1 in d:
            d[cur] += d[cur + 1]

        return helper(nums, d, i + 1, n)

    helper(nums, d, 0, len(nums))

    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
