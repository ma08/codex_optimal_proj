

def find_blocks(a, m):
    n = len(a)
    d = {}
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1])
            if s % m not in d:
                d[s % m] = [(i, j)]
            else:
                d[s % m].append((i, j))
    res = []
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1]) % m
            if s % m in d:
                for l, r in d[s % m]:
                    if l > j or r < i:
                        res.append((i, j))
    return res

def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    m = int(input())
    res = find_blocks(a, m)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

if __name__ == "__main__":
    main()
