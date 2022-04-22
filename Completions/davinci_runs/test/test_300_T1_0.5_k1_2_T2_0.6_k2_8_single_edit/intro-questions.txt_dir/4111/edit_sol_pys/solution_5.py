import sys
sys.setrecursionlimit(100000)


def dfs(node, parent):
    for next_node in tree[node]:
        if next_node == parent:
            continue
        dfs(next_node, node)

def dfs_color(node, parent, color):
    for next_node in tree[node]:
        if next_node == parent:
            continue
        if color == 1:
            if len(tree[next_node]) >= 2:
                dfs_color(next_node, node, 0)
            else:
                dfs_color(next_node, node, 1)
        else:
            dfs_color(next_node, node, 1)

# ans = 0
# for i in range(n):
#     ans += find_good_candies(n, a[:i] + a[i+1:])

# print(ans)

odd, even = 0, 0
for i in range(n):
    if i%2 == 0:
        odd += a[i]
    else:
        even += a[i]

ans = 0
for i in range(n):
    if i%2 == 0:
        if odd - a[i] == even:
            ans += 1
    else:
        if odd == even - a[i]:
            ans += 1

print(ans)
