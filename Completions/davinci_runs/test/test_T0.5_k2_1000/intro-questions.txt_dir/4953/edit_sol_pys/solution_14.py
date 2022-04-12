
import fileinput

def main():
    # read input
    lines = [line.strip() for line in fileinput.input()] # read all lines
    n = int(lines[0])
    lines = lines[1:] # ignore first line
    people = []
    for line in lines:
        name, language = line.split()[:2]
        languages = set()
        for l in line.split()[2:]: # add all languages to set
            languages.add(l)
        people.append((name, language, languages)) # add person to list

    # construct graph
    graph = {}
    for person in people:
        graph[person[0]] = [] # initialize adjacency list for each person
        for person2 in people:
            if person[0] != person2[0] and person[1] in person2[2] and person2[1] in person[2]: # if they speak each other's language
                graph[person[0]].append(person2[0]) # add to adjacency list

    # find connected components
    components = []
    visited = set()
    for person in people:
        if person[0] not in visited:
            visited.add(person[0])
            component = set()
            component.add(person[0])
            dfs(graph, person[0], visited, component) # perform dfs
            components.append(component)

    # find the smallest connected component
    min_component = min(components, key=lambda c: len(c)) # find the smallest component

    print(len(people) - len(min_component)) # print the number of people not in the smallest component

def dfs(graph, node, visited, component):
    for neighbor in graph[node]: # for each neighbor
        if neighbor not in visited:
            visited.add(neighbor) # add to visited
            component.add(neighbor) # add to component
            dfs(graph, neighbor, visited, component) # recurse

if __name__ == '__main__':
    main()
