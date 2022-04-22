

def find_blocks(a):
    n = len(a)
    d = []
    for i in range(n):
        for j in range(i, n):
            d.append((sum(a[i:j+1]), i, j))
    d.sort(key=lambda x: x[0])
    res = []
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1])
            if s in d:
                for l, r in d[s]:
                    if l > j or r < i:
                        res.append((i, j))
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
