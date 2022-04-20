
def main():
    """main function"""
    num_person = int(input())
    graph = {}
    for person in range(num_person):
        graph[person + 1] = []
        num_testimony = int(input())
        for _ in range(num_testimony):
            x_ij, y_ij = map(int, input().split())
            graph[person + 1].append((x_ij, y_ij))
    print(solve(graph))


def solve(graph_):
    """solve function"""
    num_honest = 0
    for person in graph_:
        if is_honest(graph_, person):
            num_honest += 1
    return num_honest


def is_honest(graph_, person, visited=set()):
    """is_honest function"""
    if person in visited or not graph_[person]:
        return False
    visited.add(person)
    for x_ij, y_ij in graph_[person]:
        if y_ij == 0:
            continue
        if not is_honest(graph_, x_ij, visited):
            return False
    return True


main()
