

n = int(input())
a = list(map(int, input().split()))

s = [0]*(n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

m = {}
for i in range(n):
    for j in range(i+1, n+1):
        m[(i, j)] = s[j] - s[i]

m = sorted(m.items(), key=lambda x: x[1])

ans = []
i = 0
while i < len(m):
    j = i
    while j < len(m) and m[i][1] == m[j][1]:
        j += 1
    ans.append([])
    for k in range(i, j):
        if ans[-1] == []:
            ans[-1].append(m[k][0])
        else:
            if m[k][0][0] > ans[-1][-1][1]:
                ans[-1].append(m[k][0])
    i = j

print(len(ans))
for i in ans:
    for j in i:
        print(j[0]+1, j[1])