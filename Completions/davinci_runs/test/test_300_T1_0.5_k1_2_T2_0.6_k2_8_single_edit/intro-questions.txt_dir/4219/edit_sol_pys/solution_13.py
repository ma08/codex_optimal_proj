
def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    num_person = int(input())
    graph = {}
    for person in range(num_person):
        graph[person + 1] = []
        num_testimony = int(input())
        for _ in range(num_testimony):
            x_ij, y_ij = map(int, input().split())
            graph[person + 1].append((x_ij, y_ij))
    print(solve(graph))

def solve(graph):
    """TODO: Docstring for solve.

    :graph: TODO
    :returns: TODO

    """
    num_honest = 0
    for person in graph:
        if is_honest(graph, person):
            num_honest += 1
    return num_honest

def is_honest(graph, person, visited=set()):
    """TODO: Docstring for is_honest.

    :graph: TODO
    :person: TODO
    :returns: TODO

    """
    if person in visited:
        return False
    visited.add(person)
    for x_ij, y_ij in graph[person]:
        if y_ij == 0:
            continue
        if not is_honest(graph, x_ij, visited):
            return False
    return True

main()
