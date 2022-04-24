from collections import defaultdict

def solve(a):
    a.sort()
    n = len(a)
    d = defaultdict(int)
    for i, ai in enumerate(a):
        d[ai] = i
    ans = 0
    for i, ai in enumerate(a):
        j = d[ai]
        if j == i:
            continue
        ans += min(abs(i - j), n - abs(i - j))
    return ans



if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))
