import sys


def main():
    n, r = map(int, sys.stdin.readline().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, sys.stdin.readline().split())
        a.append(ai)
        b.append(bi)
    l = [r]
    for i in range(n):
        l.append(l[i]+b[i])
    l = l[1:]
    for i in range(n):
        if a[i] > l[i]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
