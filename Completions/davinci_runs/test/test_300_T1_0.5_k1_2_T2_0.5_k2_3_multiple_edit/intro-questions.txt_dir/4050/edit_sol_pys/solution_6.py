
def find_block(a):
    n = len(a)
    d = {}
        s = 0
        for j in range(i, n):
            s += a[j]
            if s not in d:
                d[s] = [(i, j)]
            elif d[s][-1][0] < i:
                d[s].append((i, j))
    res_set = set()
    for i in range(n-1):
        for j in range(i+1, n):
            s = sum(a[i:j])
            for l, k in d[s]:
                if k < i and j < l:
                    res_set.add((i, j))
    return list(res_set)


def main():
    n = int(input().strip())
    a = [int(s) for s in input().strip().split()]
    res = find_block(a)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)


if __name__ == "__main__":
    main()
