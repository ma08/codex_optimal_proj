# Задача на программирование: количество компонент связности
# Дан невзвешенный неориентированный граф. В графе может быть несколько кратчайших путей между какими-то вершинами. Найдите количество различных компонент связности в графе.
#
# Sample Input:
#
# 4 2
# 1 2
# 3 2
# Sample Output:
# 2
#
# Sample Input 2:
#
# 4 3
# 1 2
# 3 2
# 4 3
# Sample Output 2:
#
# 1

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dfs(v, used):
    used.add(v)
    for u in graph[v]:
        if u not in used:
            dfs(u, used)


used = set()
components = 0

for v in range(n):
    if v not in used:
        dfs(v, used)
        components += 1

print(components)
