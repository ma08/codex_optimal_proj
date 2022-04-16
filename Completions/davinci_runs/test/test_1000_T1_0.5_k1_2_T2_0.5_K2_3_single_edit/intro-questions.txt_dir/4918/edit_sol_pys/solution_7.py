

#union find template

#find root of x
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

#union x and y
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[x] = y
        sizes[y] += sizes[x]
        sizes[x] = 0

#number of nodes and queries
n, q = map(int, input().split())

#read input
parents = [i for i in range(n)]
sizes = [1 for i in range(n)]

#run all queries
for i in range(q):
    query = input().split()
    if query[0] == 'u':
        union(int(query[1])-1, int(query[2])-1)
    else:
        print(sizes[find(int(query[1])-1)])
