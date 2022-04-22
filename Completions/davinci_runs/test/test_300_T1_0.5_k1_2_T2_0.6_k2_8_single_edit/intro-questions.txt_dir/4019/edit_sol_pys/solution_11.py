

n, m, D = [int(x) for x in input().split()]
edges = []
for i in range(m):
    v, u = [int(x) for x in input().split()]
    edges.append((v, u))
    edges.append((u, v))

if D > n - 1 or D < 1 or not m >= n - 1:
    print("NO")
    exit()

if D == 1:
    print("YES")
    for i in range(n - 1):
        print(edges[i][0], edges[i][1])
    exit()

if D == n - 1:
    print("YES")
    for i in range(n - 1):
        print(edges[i][1], edges[i][0])
    exit()

# D = 2
if D == 2:
    if n == 3:
        print("YES")
        print(edges[0][0], edges[0][1])
        print(edges[1][0], edges[1][1])
        exit()
    print("NO")
    exit()

# D = 3
if D == 3:
    print("NO")
    exit()

# D = 4
if D == 4:
    print("NO")
    exit()

# D = 5
if D == 5:
    print("NO")
    exit()
