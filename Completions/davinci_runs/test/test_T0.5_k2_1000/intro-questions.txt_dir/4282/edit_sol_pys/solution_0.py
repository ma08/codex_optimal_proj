
from collections import defaultdict


def solve(n, a_list):
    d = defaultdict(set)
    for i in range(n):
        d[a_list[i][0]].add(i)
        d[a_list[i][1]].add(i)
    start = 1
    for i in range(n):
        if len(d[i]) == 1:
            start = i
            break
    res = []
    for i in range(n):
        res.append(start)
        start = a_list[start][0] if a_list[start][0] != res[-1] else a_list[start][1]
    return ' '.join(map(str, res))


n = int(input())
a_list = defaultdict(list)
for i in range(n):
    a_list[i + 1] = list(map(int, input().split()))
print(solve(n, a_list))
