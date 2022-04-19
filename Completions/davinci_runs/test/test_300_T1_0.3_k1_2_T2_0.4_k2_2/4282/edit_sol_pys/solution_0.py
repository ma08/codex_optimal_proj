

from collections import defaultdict

def solve(n, a):
    graph = defaultdict(list)
    for i in range(n):
        graph[a[i][0]].append(a[i][1])
        graph[a[i][1]].append(a[i][0])
    for i in range(1, n + 1):
        if len(graph[i]) != 2:
            start = i
            break
    else:
        start = 1
    res = [start]
    curr = start
    while len(res) != n:
        for i in graph[curr]:
            if i not in res:
                res.append(i)
                curr = i
                break
    return res

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split()))
    print(*solve(n, a))
