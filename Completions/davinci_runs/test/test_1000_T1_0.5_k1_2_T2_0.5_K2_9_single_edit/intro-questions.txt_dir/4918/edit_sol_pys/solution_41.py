

#union find for problem 7

#find root of node
def find(n):
    if n == parents[n]:
        return n
    parents[n] = find(parents[n])
    return parents[n]

#union two nodes
def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    if n1 != n2:
        parents[n1] = n2
        sizes[n2] += sizes[n1]
        sizes[n1] = 0

#read input
n, q = map(int, input().split())
parents = [i for i in range(n)]
sizes = [1 for i in range(n)]

#run queries
for i in range(q):
    query = input().split()
    if query[0] == 't':
        union(int(query[1])-1, int(query[2])-1)
    else:
        print(sizes[find(int(query[1])-1)])
