

def dfs(s, A, i, res):
    if len(s) == 0:
        s.append(i+1)
        return
    if A[i] >= len(s):
        s.append(i+1)
    else:
        s.insert(A[i], i+1)
    if len(s) == N:
        res.append(s)
        return
    for j in range(N):
        if j not in s:
            dfs(s, A, j, res)
            s.pop()



N = int(input())
A = list(map(int, input().split()))

if A[0] != 0:
    print(0)
    exit()

#if len(set(A)) != N:
#    print(0)
#    exit()

s = []
for i in range(N):
    if len(s) == 0:
        s.append(i+1)
        continue
    if A[i] >= len(s):
        s.append(i+1)
    else:
        s.insert(A[i], i+1)

print(s)
