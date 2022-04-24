
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

    for i in nums:
        if i - 1 in d:
            d[i] += d[i - 1]
        if i + 1 in d:
            d[i] += d[i + 1]


    res = max(d.values())
    print(res)
    print(' '.join([str(i) for i in nums if d[i] == res]))

if __name__ == '__main__':
    main()
