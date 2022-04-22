

def main():
    """main function"""
    num_person = int(input())
    graph = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
    }
    for person in range(num_person):
        num_testimony = int(input())
        for _ in range(num_testimony):
            x_ij, y_ij = map(int, input().split()) # pylint: disable=W0612
            graph[person + 1].append((x_ij, y_ij))
    print(solve(graph))

def solve(graph): # pylint: disable=R0912
    """solve function"""
    num_honest = 0
    for person in graph:
        if is_honest(graph, person):
            num_honest += 1
    return num_honest

def is_honest(graph, person, visited=set()):
    """is_honest function"""
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

# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
