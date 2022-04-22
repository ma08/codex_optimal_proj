
def find_blocks(a):
    d = {0: [-1]}
    s = 0
    res = 0
    for i in range(len(a)):
        s += a[i]
        if s in d:
            for j in d[s]:
                res += i - j
        if s not in d:
            d[s] = [i]
        else:
            d[s].append(i)
    return res - 1


def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    res = find_blocks(a)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

if __name__ == "__main__":
    main()
