
import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    c = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    b.sort()
    c.sort()
    i = j = k = 0
    count = 0
    while j < len(b):
        while i < len(a) and a[i] <= b[j]:
            i += 1
        while k < len(c) and c[k] <= b[j]:
            k += 1
        count += i * k
        j += 1
    print(count)


if __name__ == '__main__':
    main()
