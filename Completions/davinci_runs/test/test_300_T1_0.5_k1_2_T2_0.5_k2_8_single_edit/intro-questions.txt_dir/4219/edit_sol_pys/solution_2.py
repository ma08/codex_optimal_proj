

def main():
    """main function"""
    num_person = int(input())
    graph = {}
    for person in range(num_person):
        graph[person + 1] = []
        num_testimony = int(input())
        for _ in range(num_testimony):
            x_i, y_i = map(int, input().split())
            graph[person + 1].append((x_i, y_i))
    print(solve(graph))

def solve(graph):
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
    for x_i, y_i in graph[person]:
        if y_i == 0:
            continue
        if not is_honest(graph, x_ij, visited):
            return False
    return True

main()
