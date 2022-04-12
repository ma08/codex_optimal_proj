

def find_blocks(a, b):
    n = len(a)
    d = {0: [(-1, -1)]}
    s = 0
    for i in range(n):
        s += a[i]
        if s not in d:
            d[s] = [(i, i+1)]
        else:
            d[s].append((i, i+1))
    res = []
    for i in range(n-1):
        for j in range(i+1, n):
            s = sum(a[i:j])
            if s in d and d[s][0][0] < i:
                res.append((i, j-1))
    return res

def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    res = find_blocks(a, b)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

if __name__ == "__main__":
    main()
