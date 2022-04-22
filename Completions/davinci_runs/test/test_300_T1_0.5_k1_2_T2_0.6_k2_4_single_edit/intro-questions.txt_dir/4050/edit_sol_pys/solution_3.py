

def find_blocks(a):
    n = len(a)
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            s = sum(a[i:j])
            if (s, i) not in d:
                d[(s, i)] = [(i, j)]
            else:
                d[(s, i)].append((i, j))
    res = []
    for i in range(n):
        for j in range(i+1, n):
            s = sum(a[i:j])
            if (s, j) in d:
                for l, r in d[(s, j)]:
                    if l > i or r < j:
                        res.append((i, j-1))
    return res

def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    res = find_blocks(a)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

if __name__ == "__main__":
    main()
