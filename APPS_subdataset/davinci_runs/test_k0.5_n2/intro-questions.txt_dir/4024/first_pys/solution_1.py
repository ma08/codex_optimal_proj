

from collections import defaultdict

def solve(n, k, s):
    count = defaultdict(int)
    for i in range(n):
        count[s[i]] += 1
    if k > n:
        return -1
    if k == n:
        return sum(count.values())
    if k == 1:
        return n - max(count.values())
    if k == 2:
        return sum(count.values()) - max(count.values())
    return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))