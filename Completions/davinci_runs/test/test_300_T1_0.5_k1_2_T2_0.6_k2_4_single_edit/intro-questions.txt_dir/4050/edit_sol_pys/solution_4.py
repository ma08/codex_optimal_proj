

    f = open('input.txt', 'r')
    f.readline()
    a = [int(x) for x in f.readline().split()]
    f.close()
    f = open('output.txt', 'w')
def main():
    n = int(input())
    sums = [0]
    for i in a:
        sums.append(sums[-1] + i)
    sums.append(sums[-1])
    blocks = []
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])
    blocks.sort(key=lambda x: x[2])
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
    f.write(str(len(res)) + '\n')
    for i in res:
        print(i[0] + 1, i[1])

main()
