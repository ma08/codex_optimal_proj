
def main():
    n, r = map(int, input().split())  # n: number of days, r: initial health
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())  # ai: minimum health, bi: health gained
        a.append(ai)
        b.append(bi)
    l = [r]
    for i in range(n):
        l.append(l[i] + b[i])
    l = l[1:]
    for i in range(n):
        if a[i] > l[i]:
            print("NO")
            return
    print("YES")
    return


if __name__ == '__main__':
    main()
