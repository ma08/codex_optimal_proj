

from collections import defaultdict


def main():
    n = int(input())
    a = defaultdict(list)
    for i in range(n):
        x, y = map(int, input().split())
        a[x].append(i + 1)
        a[y].append(i + 1)
    p = [-1] * n
    p[0] = 1
    p[2] = a[1][0]
    for i in range(3, n):
        p[i] = a[p[i - 1]][0] if a[p[i - 1]][0] != p[i - 2] else a[p[i - 1]][1]
    print(*p)


if __name__ == '__main__':
    main()
