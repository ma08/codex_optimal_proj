

def merge(a, b):
    if a[0] <= b[0] and b[1] <= a[1]:
        return a
    if b[0] <= a[0] and a[1] <= b[1]:
        return b
    if b[0] <= a[0] and a[0] <= b[1]:
        if a[1] <= b[1]:
            return [b[0], a[1]]
        else:
            return b
    if a[0] <= b[0] and b[0] <= a[1]:
        if b[1] <= a[1]:
            return [a[0], b[1]]
        else:
            return a
    return None

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    sums = [0] + [0]*n
    for i in range(n):
        sums[i+1] = sums[i] + a[i]
    blocks = []
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])
    blocks.sort(key=lambda x: x[2])
    for i in range(len(blocks)):
        for j in range(i+1, len(blocks)):
            if blocks[j][0] < blocks[i][1]:
                blocks[i] = merge(blocks[i], blocks[j])
                blocks.pop(j)
                j -= 1
    blocks.sort(key=lambda x: x[1])
    res = []
    while len(blocks) > 0:
        i = blocks[0][0]
        j = blocks[0][1]
        blocks.pop(0)
        res.append([i, j])
        for k in range(len(blocks)):
            if blocks[k][0] < j:
                blocks.pop(k)
                k -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])

main()
