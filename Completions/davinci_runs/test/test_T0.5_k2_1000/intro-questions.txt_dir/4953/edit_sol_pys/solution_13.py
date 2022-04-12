

from collections import defaultdict

def dfs(graph, visited, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)

def solve(patrons):
    graph = defaultdict(list)
    for patron in patrons:
        for language in patrons[patron]:
            for other_patron in patrons:
                if patron != other_patron and language in patrons[other_patron]:
                    graph[patron].append(other_patron)
                    graph[other_patron].append(patron)

    visited = defaultdict(bool)
    components = 0
    for patron in graph:
        if not visited[patron]:
            dfs(graph, visited, patron)
            components += 1
    return components

def main():
    num_patrons = int(input())
    patrons = defaultdict(set)
    for i in range(num_patrons):
        patron, language, *other_languages = input().split(' ')
        patrons[patron].add(language)
        for other_language in other_languages:
            patrons[patron].add(other_language)
    print(solve(patrons))

if __name__ == "__main__":
    main()
