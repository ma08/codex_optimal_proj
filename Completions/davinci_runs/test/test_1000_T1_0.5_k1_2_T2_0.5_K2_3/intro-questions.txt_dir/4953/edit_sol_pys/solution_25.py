
from collections import defaultdict

def dfs(graph, visited, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)

def solve(students):
    graph = defaultdict(list)
    for student in students:
        for language in students[student]:
            for other_student in students:
                if student != other_student and language in students[other_student]:
                    graph[student].append(other_student)
                    graph[other_student].append(student)

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
        patron, language, *other_languages = input().split()
        patrons[patron].add(language)
        for other_language in other_languages:
            patrons[patron].add(other_language)
    print(solve(patrons))

if __name__ == "__main__":
    main()
