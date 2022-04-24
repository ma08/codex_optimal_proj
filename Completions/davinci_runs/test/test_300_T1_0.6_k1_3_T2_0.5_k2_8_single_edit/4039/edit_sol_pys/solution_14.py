

def main():
    n, r = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    l = [r] * (n+1)
    for i in range(n):
        if a[i] > l[i+1]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
