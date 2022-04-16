
import sys

def main():
    n, k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a, b = zip(*sorted(zip(a, b)))
    for i in range(n):
        if k <= b[i]:
            print(a[i])
            sys.exit()
        k -= b[i]

if __name__ == '__main__':
    main()
