# https://atcoder.jp/contests/abc174/tasks/abc174_c
N, M = map(int, input().split())

island = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    island[a].append(b)
    island[b].append(a)

if island[1] == []:
    print("IMPOSSIBLE")
else:
    for i in island[1]:
        if N in island[i]:
            print("POSSIBLE")
            exit()

print("IMPOSSIBLE")
