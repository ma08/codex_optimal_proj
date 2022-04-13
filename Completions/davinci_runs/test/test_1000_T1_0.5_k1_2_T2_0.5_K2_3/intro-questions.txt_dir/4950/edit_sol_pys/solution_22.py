
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    d = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            if d.get(a[i] + a[j]):
                d[a[i] + a[j]] += 1
            else:
                d[a[i] + a[j]] = 1

    print(max(d.values()))

if __name__ == '__main__':
    main()
