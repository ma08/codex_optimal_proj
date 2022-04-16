import collections

def main():
    n, m = map(int, input().split())
    d = collections.defaultdict(list)
    for i in range(n):
        d[input()].append(i+1)
    for i in range(m):
        s = input()
        if s in d:
            print(' '.join(map(str, d[s])))
        else:
            print(-1)

if __name__ == "__main__":
    main()
