

n = int(input())
a = []
for i in range(n):
    x = input().split(' ')
    a.append([int(x[0]), int(x[1])])

# print(a)

def make_graph(a):
    g = {}
    for i in range(len(a)):
        if a[i][0] not in g:
            g[a[i][0]] = [a[i][1]]
        else:
            g[a[i][0]].append(a[i][1])

        if a[i][1] not in g:
            g[a[i][1]] = [a[i][0]]
        else:
            g[a[i][1]].append(a[i][0])
    # print(g)
    return g

def dfs(g, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(g[vertex]) - set(visited))
    return visited

g = make_graph(a)
# print(g)

# print(dfs(g, 1))

visited = dfs(g, 1)

def get_path(g, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(g[vertex]) - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

visited.sort()

for i in range(len(visited)):
    if i == 0:
        path = list(get_path(g, visited[i], visited[i+1]))
    elif i == len(visited)-1:
        path = list(get_path(g, visited[i], visited[0]))
    else:
        path = list(get_path(g, visited[i], visited[i+1]))
    # print(path)
    for j in range(len(path)):
        if len(path[j]) == 2:
            path[j] = [path[j][1], path[j][0]]
    # print(path)
    visited = list(set(visited) - set(path[0]))
    visited = path[0] + visited

print(' '.join(map(str, visited)))