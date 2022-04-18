

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
    for student in graph:
        if not visited[student]:
            dfs(graph, visited, student)
            components += 1
    return components

def main():
    num_students = int(input())
    students = defaultdict(set)
    for i in range(num_students):
        student, language, *other_languages = input().split()
        students[student].add(language)
        for other_language in other_languages:
            students[student].add(other_language)
    print(solve(students))

if __name__ == "__main__":
    main()
