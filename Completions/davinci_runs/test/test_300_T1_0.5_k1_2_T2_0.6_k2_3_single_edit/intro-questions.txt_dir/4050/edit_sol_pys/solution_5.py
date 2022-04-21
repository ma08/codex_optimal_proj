import sys


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    res = find_blocks(a)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

def find_blocks(a, n):
    n = len(a)
    d = {}
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1])
            if s not in d:
                d[s] = [(i, j)]
            else:
                d[s].append((i, j))
    res = []
    for i in range(n):
        for j in range(i, n):
            s = sum(a[i:j+1])
            if s in d:
                for l, r in d[s]:
                    if l > j or r < i:
                        res.append((i, j))
    return res

if __name__ == "__main__":
    main()
