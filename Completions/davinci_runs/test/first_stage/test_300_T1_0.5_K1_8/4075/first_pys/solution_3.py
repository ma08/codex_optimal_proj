

from collections import defaultdict

def main():
    n, m = map(int, input().split())
    bulbs = defaultdict(set)
    for i in range(1, m + 1):
        k, *s = map(int, input().split())
        bulbs[i] = set(s)
    p = list(map(int, input().split()))
    c = 0
    for i in range(2 ** n):
        valid = True
        for j in range(1, m + 1):
            on = sum(1 if i & (1 << (s - 1)) > 0 else 0 for s in bulbs[j])
            if not on % 2 == p[j - 1]:
                valid = False
        if valid:
            c += 1
    print(c)

if __name__ == '__main__':
    main()