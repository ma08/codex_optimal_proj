def binarySearch(a, x):
    left = 0
    right = len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left

def main():
    n = int(input())
    a.sort()
    a = [int(x) for x in input().split()]
    sums = [0]
    for i in range(n):
        sums.append(sums[-1] + a[i])
    sums.append(sums[-1])
    blocks = []
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])
    blocks.sort(key=lambda x: x[1])
    blocks.sort(key=lambda x: x[2])
    res = []
    while len(blocks) > 0:
        i, j, _ = blocks[0]
        blocks.pop(0)
        res.append([i+1, j])
        for k in range(len(blocks)):
            if blocks[k][1] <= j:
                blocks.pop(k)
                k -= 1
    print(len(res))
    for i, j in res:
        print(i, j)

main()
