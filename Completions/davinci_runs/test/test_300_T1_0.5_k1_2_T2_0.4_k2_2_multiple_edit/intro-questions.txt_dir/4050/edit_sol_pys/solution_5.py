
def find_blocks(arr):
    n = len(arr)
    d = {}
    for i in range(n):
        for j in range(i, n):
            s = sum(arr[i:j + 1])
            if s not in d:
                d[s] = [(i, j)]
            else:
                d[s].append((i, j))
    res = []
    for i in range(n):
        for j in range(i, n):
            s = sum(arr[i:j + 1])
            if s in d:
                for l, r in d[s]:
                    if l > j or r < i:
                        res.append((i, j))
    return res


def main():
    n = int(input())
    arr = [int(s) for s in input().split()]
    res = find_blocks(arr)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)


if __name__ == "__main__":
    main()
