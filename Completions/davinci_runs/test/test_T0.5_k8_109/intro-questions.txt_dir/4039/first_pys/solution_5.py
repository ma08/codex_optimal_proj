

import sys

def main():
    n, r = [int(x) for x in sys.stdin.readline().split()]
    a = []
    b = []
    for i in range(n):
        ai, bi = [int(x) for x in sys.stdin.readline().split()]
        a.append(ai)
        b.append(bi)
    for i in range(n):
        if r < a[i]:
            print("NO")
            return
        r += b[i]
        if r < 0:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()