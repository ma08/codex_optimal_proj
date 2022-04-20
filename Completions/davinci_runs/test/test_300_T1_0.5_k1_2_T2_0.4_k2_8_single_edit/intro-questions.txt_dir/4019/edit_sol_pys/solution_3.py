
n, m, D = [int(x) for x in input().split()]
edges = []
for i in range(m):
    v, u = [int(x) for x in input().split()]
    edges.append((v, u))
    edges.append((u, v))

if D > n - 1 or D < 1 or not m >= n - 1:
    print("NO")
    exit

if D == 1:
    print("YES")
    for i in range(n - 1):
        print(edges[i][0], edges[i][1])
    exit

if D == n - 1:
    print("YES")
    for i in range(n - 1):
        print(edges[i][1], edges[i][0])
    exit

# D = 2
if D == 2:
    if n == 3:
        print("YES")
        print(edges[0][0], edges[0][1])
        print(edges[1][0], edges[1][1])
        exit
    if n == 4:
        if m == 3:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[3][0], edges[3][1])
            exit

# D = 3
if D == 3:
    if n == 4:
        if m == 3:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[2][0], edges[2][1])
            exit
    if n == 5:
        if m == 4:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[2][0], edges[2][1])
            print(edges[4][0], edges[4][1])
            exit
    if n == 6:
        if m == 5:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[2][0], edges[2][1])
            print(edges[3][0], edges[3][1])
            print(edges[5][0], edges[5][1])
            exit

# D = 4
if D == 4:
    if n == 5:
        if m == 4:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[2][0], edges[2][1])
            print(edges[3][0], edges[3][1])
            exit
    if n == 6:
        if m == 5:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[2][0], edges[2][1])
            print(edges[3][0], edges[3][1])
            print(edges[4][0], edges[4][1])
            exit

# D = 5
if D == 5:
    if n == 6:
        if m == 5:
            print("NO")
            exit
        else:
            print("YES")
            print(edges[0][0], edges[0][1])
            print(edges[1][0], edges[1][1])
            print(edges[2][0], edges[2][1])
            print(edges[3][0], edges[3][1])
            print(edges[4][0], edges[4][1])
            exit
