

n, m = [int(i) for i in input().split()] # n = number of nodes, m = number of edges

if m == n - 1:
    print(m) # if there is no cycle, it is a tree
elif m <= n:
    print(m + 1) # if there is a cycle, it is a forest
else:
    print(n + (m - n) // 2)
