#!/usr/bin/env python3

import fileinput

def main():
    # read input
    lines = [line.strip() for line in fileinput.input()]
    n = int(lines[0])
    lines = lines[1:]
    people = []
    for line in lines:
        name, language = line.split()
        languages = set()
        for l in line.split()[2:]:
            languages.add(l)
        people.append((name, language, languages))

    # construct graph
    graph = {}
    for person in people:
        graph[person[0]] = []
        for person2 in people:
            if person[0] != person2[0] and person[1] in person2[2] and person2[1] in person[2]:
                graph[person[0]].append(person2[0])

    # find connected components
    components = []
    visited = set()
    for person in people:
        if person[0] not in visited:
            visited.add(person[0])
            component = set()
            component.add(person[0])
            dfs(graph, person[0], visited, component)
            components.append(component)

    # find the smallest connected component 
    min_component = min(components, key=lambda c: len(c))

    print(len(people) - len(min_component) - 1)

def dfs(graph, node, visited, component):
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            component.add(neighbor)
            dfs(graph, neighbor, visited, component)

if __name__ == '__main__':
    main()
