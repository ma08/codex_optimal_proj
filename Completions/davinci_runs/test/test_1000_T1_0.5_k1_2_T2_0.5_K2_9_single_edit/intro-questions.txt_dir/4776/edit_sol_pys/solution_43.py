



#%%
import sys
sys.setrecursionlimit(10**7)


#%%
N, M = map(int, input().split())


#%%
L = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)


#%%
def dfs(v, t, visited):
    if visited[v]:
        return False
    visited[v] = True
    if v == t:
        return True
    for i in L[v]:
        if dfs(i, t, visited):
            return True
    return False


#%%
def main():
    for i in range(N):
        visited = [False for i in range(N)]
        if not dfs(0, i, visited):
            return 'No'
    return 'Yes'


#%%
print(main())


#%%
#%%
N = int(input())

start = []
end = []

for i in range(N):
    s, t = map(int, input().split())
    start.append(s)
    end.append(t)

start.sort()
end.sort()

#%%
total = 0
i = 0
j = 0
while i < N:
    if start[i] <= end[j]:
        total += start[i] - end[j] + 1
        i += 1
    else:
        j += 1

print(total)

#%%
