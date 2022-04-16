

from collections import Counter

def solve(n, k, m, a):
    c = Counter(a)
    c = sorted(c.items(), key=lambda x: x[0])
    total = 0
    for i in range(len(c)):
        if c[i][1] > m:
            total += c[i][0] * m
            m = 0
        else:
            total += c[i][0] * c[i][1]
            m -= c[i][1]
    return total

def main():
    for _ in range(int(input())):
        n, k, m = map(int, input().split())
        a = list(map(int, input().split()))
        ans = solve(n, k, m, a)
        print(ans)

if __name__ == '__main__':
    main()
