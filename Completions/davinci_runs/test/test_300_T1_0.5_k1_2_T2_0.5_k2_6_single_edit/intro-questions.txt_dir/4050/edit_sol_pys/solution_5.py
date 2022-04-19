

def find_blocks(a, n):
    d = {}  # d[i] = the number of blocks ending at i
    for i in range(n-1, -1, -1):
        if i == n-1:
            d[i] = 1
        elif a[i] == a[i+1]:
            d[i] = d[i+1] + 1
        else:
            d[i] = 1
    return d

def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    # res = find_blocks(a, n)
    # for i in range(n):
    #     print(res[i], end=' ')
    # print()
    p = [0] * n
    for i in range(n):
        if i == 0:
            p[i] = 1
        elif a[i] == a[i-1]:
            p[i] = p[i-1] + 1
        else:
            p[i] = 1
    # for i in range(n):
    #     print(p[i], end=' ')
    # print()
    res = 0
    for i in range(n):
        for j in range(i, n):
            if a[j] == a[i]:
                res += 1
            else:
                break
    print(res)

if __name__ == "__main__":
    main()
