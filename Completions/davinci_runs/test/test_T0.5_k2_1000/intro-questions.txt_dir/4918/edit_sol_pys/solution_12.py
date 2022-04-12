

def main():
    # get input, use readline() to read from file
    n, q = map(int, sys.stdin.readline().split())
    queries = []
    for i in range(q):
        queries.append(sys.stdin.readline().split())

    # initialize
    group_sizes = [1]*n
    group_leader = [i for i in range(n)]

    # process queries
    for query in queries:
        # merge groups 
        if query[0] == 't':
            a = int(query[1])-1
            b = int(query[2])-1
            leader_a = find_leader(a, group_leader)
            leader_b = find_leader(b, group_leader)
            if leader_a != leader_b:
                group_sizes[leader_b] += group_sizes[leader_a]
                group_leader[leader_a] = leader_b
        # print size of group
        else:
            a = int(query[1])-1
            leader_a = find_leader(a, group_leader)
            print(group_sizes[leader_a], end='')

def find_leader(a, group_leader):
    while group_leader[a] != a:
        a = group_leader[a]
    return a

main()
