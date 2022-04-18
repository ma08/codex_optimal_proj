import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    d = {}
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]
    for i in range(1, n + 1):
        if i in d:
            print(len(d[i]) - 1)
        else:
            print(0)

if __name__ == '__main__':
    main()
