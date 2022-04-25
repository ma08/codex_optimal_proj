"""
CODING CHALLENGE:
There are n people in a town. Each person has a
list of people that he or she trusts. For example,
if there are 4 people, the list of trust might be
[[1,2], [2,3], [3,4], [4,1]].
This means that person 1 trusts person 2, person 2
trusts person 3, person 3 trusts person 4, and
person 4 trusts person 1.
We want to find out how many people in this town
are honest. An honest person is one who tells the
truth about who he or she trusts. A dishonest
person is one who lies about who he or she trusts.
For example, if person 1 says that he or she trusts
person 2, but person 2 says that he or she doesn't
trust person 1, then person 1 is dishonest.
Write a function that takes in a list of trust
relationships (e.g. [[1,2], [2,3], [3,4], [4,1]])
and prints out the number of honest people in the
town.
"""

def main():
    """
    main function
    """
    num_persons = int(input())
    graph = {}
    for person in range(num_persons):
        graph[person + 1] = []
        num_testimony = int(input())
        for _ in range(num_testimony):
            x_ij, y_ij = map(int, input().split())
            graph[person + 1].append((x_ij, y_ij))
    print(solve(graph))

def solve(graph):
    """
    solve function
    """
    num_honest = 0
    for person in graph:
        if is_honest(graph, person):
            num_honest += 1
    return num_honest

def is_honest(graph, person, visited=set()):
    """
    is_honest function
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
