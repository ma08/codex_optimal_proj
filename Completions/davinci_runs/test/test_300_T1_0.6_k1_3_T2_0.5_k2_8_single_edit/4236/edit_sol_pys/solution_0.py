
n, m = map(int, input().split())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))

l = set()
for i in range(n):
    for j in range(segments[i][0], segments[i][1] + 1):
        l.add(j)

l = list(l)
l.sort()

for i in l:
    for j in range(n):
        if i in range(segments[j][0], segments[j][1] + 1):
            l.remove(i)
            break

print(len(l))
for i in l:
    print(i, end=' ')
