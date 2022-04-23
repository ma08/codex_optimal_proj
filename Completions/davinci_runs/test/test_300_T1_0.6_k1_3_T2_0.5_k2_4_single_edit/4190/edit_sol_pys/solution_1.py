from collections import defaultdict


def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()] + [0]
    b = [int(x) for x in input().split()] + [0]
    d = defaultdict(lambda: 0)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] += 1
    for x in d:
        if d[x] % 2 == 1:
            print('NO')
            return
    print('YES')

if __name__ == '__main__':
    main()
