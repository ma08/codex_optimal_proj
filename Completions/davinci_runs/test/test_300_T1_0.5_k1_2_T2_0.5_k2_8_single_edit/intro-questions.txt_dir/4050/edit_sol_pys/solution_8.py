

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
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
    ans = []
    i = 0
    while i < len(blocks):
        a = blocks[i][0]
        b = blocks[i][1]
        ans.append([a, b])
        i += 1
        while i < len(blocks) and blocks[i][0] < b:
            i += 1
    print(len(ans))
    for i in ans:
        print(i[0] + 1, i[1], sep=' ')

main()
