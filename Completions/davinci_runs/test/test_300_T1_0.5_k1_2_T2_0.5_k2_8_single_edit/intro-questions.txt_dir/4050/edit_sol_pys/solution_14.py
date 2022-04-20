

def find_blocks(a):
    n = len(a)
    d = {}
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1])
            if s not in d:
                d[s] = [(i, j)]
            else:
                d[s].append((i, j))
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
    for i, j in res:
        print(i+1, j+1)

if __name__ == "__main__":
    main()
