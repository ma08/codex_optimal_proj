
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    if k == 1:
        print(sum(a))
        return
    a.sort(reverse=True)
    m = a[0]
    a = a[1:]
    a.sort()
    for i in range(k - 1):
        m += a[i]
    print(m)

if __name__ == '__main__':
    main()
