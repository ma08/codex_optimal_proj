
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort()
    if a[0] > b[0]:
        print("-1")
    else:
        count = 0
        i = 0
        j = 0
        while i < n and j < m:
            if a[i] > b[j]:
                count += 1
                j += 1
            i += 1
        print(count)

if __name__ == "__main__":
    main()
