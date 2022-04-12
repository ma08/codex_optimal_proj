

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    sums = [0]  # sums[i] = sum(a[0], a[1], ..., a[i-1]) for i in range(n+1)
    for i in a:
        sums.append(sums[-1] + i)  # sums[i] = sum(a[0], a[1], ..., a[i-1]) for i in range(n)
    sums.append(sums[-1])  # sums[n] = sum(a[0], a[1], ..., a[n-1])
    blocks = []
    for i in range(n):
        for j in range(i+1, n+1):
            blocks.append([i, j, sums[j] - sums[i]])  # blocks[i] = [i, j, sum(a[i], a[i+1], ..., a[j-1])] for i in range(n)
    blocks.sort(key=lambda x: x[2])
    blocks.sort(key=lambda x: x[1])  # blocks[i] = [i, j, sum(a[i], a[i+1], ..., a[j-1])] for i in range(n)
    res = []
    while len(blocks) > 0:
        i = blocks[0][0]
        j = blocks[0][1]
        blocks.pop(0)
        res.append([i, j])  # res[i] = [i, j]
        for k in range(len(blocks)):
            if blocks[k][0] < j:
                blocks.pop(k)
                k -= 1
    print(len(res))
    for i in res:
        print(i[0] + 1, i[1])

main()
