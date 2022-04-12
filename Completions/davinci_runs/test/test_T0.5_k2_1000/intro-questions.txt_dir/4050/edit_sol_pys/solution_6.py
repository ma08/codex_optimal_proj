

def find_blocks(a):
    n = len(a)
    s = 0
    d = {0: [-1]}
    for i in range(n):
        s += a[i]
        if s not in d:
            d[s] = [i]
        else:
            d[s].append(i)
    return d

def find_subarrays(d):
    res = 0
    for v in d.values():
        n = len(v)
        res += n*(n-1)//2
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
