

from collections import defaultdict

def dfs(graph, visited, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)

def solve(patron):
    graph = defaultdict(list)
    for person in patron:
        for language in patron[person]:
            for other_person in patron:
                if person != other_person and language in patron[other_person]:
                    graph[person].append(other_person)
                    graph[other_person].append(person)

    visited = defaultdict(bool)
    components = 0
    for person in graph:
        if not visited[person]:
            dfs(graph, visited, person)
            components += 1
    return components

def main():
    num_patrons = int(input())
    patron = defaultdict(set)
    for i in range(num_patrons):
        patron, language, *other_languages = input().split()
        patron[patron].add(language)
        for other_language in other_languages:
            patron[patron].add(other_language)
    print(solve(patron))

if __name__ == "__main__":
    main()
