

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    res = 0
    for k in d:
        if len(d[k]) == 1:
            res += 1
        else:
            res += len(d[k]) // 2
    print(res)

if __name__ == '__main__':
    main()