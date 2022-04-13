

from collections import defaultdict, namedtuple

def dfs(graph, visited, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)

def solve(patron):
    graph = defaultdict(list)
    for p in patron:
        for language in patron[p]:
            for other_patron in patron:
                if p != other_patron and language in patron[other_patron]:
                    graph[p].append(other_patron)
                    graph[other_patron].append(p)

    visited = defaultdict(bool)
    components = 0
    for p in graph:
        if not visited[p]:
            dfs(graph, visited, p)
            components += 1
    return components

def main():
    num_patrons = int(input())
    patron = defaultdict(set)
    for i in range(num_patrons):
        p, language, *other_languages = input().split()
        patron[p].add(language)
        for o in other_languages:
            patron[p].add(o)
    print(solve(patron))

if __name__ == "__main__":
    main()
