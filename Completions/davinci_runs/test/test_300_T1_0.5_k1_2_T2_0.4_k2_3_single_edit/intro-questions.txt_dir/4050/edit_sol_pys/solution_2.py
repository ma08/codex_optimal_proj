

def main():
    n = int(input())
    a = [int(x) for x in input().split()]  # read list
    sums = [0]
    for i in a:
        sums.append(sums[-1] + i)
    sums.append(sums[-1])
    blocks = []  # list of blocks
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])
    blocks.sort(key=lambda x: x[2])  # sort by sum
    blocks.sort(key=lambda x: x[1])  # sort by right
    res = []
    while len(blocks) > 0:
        i = blocks[0][0]
        j = blocks[0][1]
        blocks.pop(0)  # remove first block
        res.append([i, j])
        for k in range(len(blocks)):
            if blocks[k][0] < j:  # remove all blocks with left < j
                blocks.pop(k)  # k is not changed
                k -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])

main()
