

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    sums = [0]
    for x in a:
        sums.append(sums[-1] + x)
    sums.append(sums[-1])
    blocks = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            blocks.append([i, j, sums[j] - sums[i], j - i])
    blocks.sort(key=lambda x: x[2])
    blocks.sort(key=lambda x: x[3])
    blocks.sort(key=lambda x: x[1])
    res = []
    while len(blocks) > 0:
        i, j, _, _ = blocks[0]
        blocks.pop(0)
        res.append([i, j])
        for i in range(len(blocks)):
            if blocks[i][0] < j:
                blocks.pop(i)
                i -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])

main()
