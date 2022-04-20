

def main():
    n, r = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    l = [r for i in range(n)]
    for i in range(n):
        l[i] += b[i]
    for i in range(n):
        if a[i] > l[i]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
