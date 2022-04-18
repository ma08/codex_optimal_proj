from collections import defaultdict

def find_leader(a, group_leader):
    while group_leader[a] != a:
        a = group_leader[a]
    return a


def main():
    # get input
    n, q = map(int, input().split())
    queries = []
    for i in range(q):
        queries.append(input().split())

    # initialize
    group_sizes = [1]*n
    group_leader = {i:i for i in range(n)}

    # process queries
    for query in queries:
        # merge groups
        if query[0] == 't' and len(query) == 3:
            a = int(query[1])-1
            b = int(query[2])-1
            leader_a = find_leader(a, group_leader.keys())
            leader_b = find_leader(b, group_leader.keys())
            if leader_a != leader_b:
                group_sizes[leader_b] += group_sizes[leader_a]
                group_leader[leader_a] = leader_b
        # print size of group
        else:
            a = int(query[1])-1
            leader_a = find_leader(a, group_leader.keys())
            print(group_sizes[leader_a])

def find_leader(a, group_leader):
    while group_leader[a] != a:
        a = group_leader[a]
    return a

main()
