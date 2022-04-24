

def main():
    n, r = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    l = [r - a[0]]
    for i in range(n):
        l.append(l[i]+b[i]-a[i])
    for i in range(n):
        if a[i] > l[i]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
