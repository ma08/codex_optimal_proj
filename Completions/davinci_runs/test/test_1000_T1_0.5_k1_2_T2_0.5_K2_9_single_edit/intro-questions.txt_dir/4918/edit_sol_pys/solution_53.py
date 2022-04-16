

def main():
    # get input
    n, q = map(int, input().split()) # number of students and queries
    queries = [] # list of queries
    for i in range(q): # get queries
        queries.append(input().split()) # query is list of query type and query parameters

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
            print(group_sizes[leader_a])

def find_leader(a, group_leader):
    while group_leader[a] != a:
        a = group_leader[a]
    return a

main()
