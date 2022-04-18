
import sys

def main():
    n, m = map(int, input().split())
    t = list(map(int, input().split()))
    l = list(map(int, input().split()))

    t.sort()
    l.sort()

    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if t[i] <= l[j]:
            count += 1
            i += 1
        j += 1
    print(count)

if __name__ == '__main__':
    main()
