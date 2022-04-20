

def find_blocks(a, k):
    n = len(a)
    d = {}
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1]) % k
            if (i, j) not in d:
                d[(i, j)] = s
            else:
                d[(i, j)] = s
    res = []
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1]) % k
            for l, r in d:
                if l > j or r < i and d[(l, r)] == s:
                    res.append((i, j))
    return res

def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    k = int(input())
    res = find_blocks(a, k)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

if __name__ == "__main__":
    main()
