

from collections import defaultdict

def dfs(graph, visited, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)

def solve(patrons):
    graph = defaultdict(list)
    for person in patrons:
        for language in patrons[person]:
            for other_person in patrons:
                if person != other_person and language in patrons[other_person]:
                    graph[person].append(other_person)
                    graph[other_person].append(person)

    visited = defaultdict(lambda: False)
    components = 0
    for person in graph:
        if not visited[person]:
            dfs(graph, visited, person)
            components += 1
    return components

def main():
    num_patrons = int(input())
    patrons = defaultdict(set)
    for i in range(num_patrons):
        patron, language, *other_languages = input().split()
        patrons[patron].add(language)
        for other_language in other_languages:
            patrons[patron].add(other_language)
    print(solve(patrons))

if __name__ == "__main__":
    main()
