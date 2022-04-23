
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    sums = [0] + list(accumulate(a)) + [sums[-1]]
    blocks = []
    for i in range(n+1):
        for j in range(i+1, n+2):
            blocks.append((i, j, sums[j] - sums[i]))
    blocks.sort(key=lambda x: x[2])
    blocks.sort(key=lambda x: x[1])
    res = set()
    for i, j, _ in blocks:
        res.add((i, j))
        for k in range(n+1):
            if k < j:
                res.add((i, k))
    print(len(list(res)))
    for i, j in res:
        print(i + 1, j)

main()
