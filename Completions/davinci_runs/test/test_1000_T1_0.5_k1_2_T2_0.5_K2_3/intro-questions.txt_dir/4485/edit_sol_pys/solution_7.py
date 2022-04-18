
# https://atcoder.jp/contests/abc174/tasks/abc174_c
n, m = map(int, input().split())

island = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    island[a].append(b)
    island[b].append(a)

for i in island[1]:
    if n in island[i]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
