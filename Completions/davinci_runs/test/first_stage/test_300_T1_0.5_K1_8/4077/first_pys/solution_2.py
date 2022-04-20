

def main():
    n,m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    counts = {}
    for i in arr:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    keys = sorted(counts.keys())
    left = 0
    right = len(keys) - 1
    res = 0
    while left <= right:
        if keys[left] + keys[right] == m:
            if keys[left] == keys[right]:
                res += counts[keys[left]] * (counts[keys[left]] - 1)
            else:
                res += counts[keys[left]] * counts[keys[right]]
            left += 1
            right -= 1
        elif keys[left] + keys[right] < m:
            left += 1
        else:
            right -= 1
    print(res)

if __name__ == '__main__':
    main()