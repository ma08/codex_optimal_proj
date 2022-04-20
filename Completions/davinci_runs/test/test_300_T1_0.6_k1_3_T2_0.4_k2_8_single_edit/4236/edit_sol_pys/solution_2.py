

n, m = map(int, input().split())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))

l = []
for i in range(n):
    for j in range(segments[i][0], segments[i][1] + 1):
        l.append(j)

l = list(set(l))
l.sort()

i = 0
while i < len(l):
    for j in range(n):
        if l[i] in range(segments[j][0], segments[j][1] + 1):
            l.pop(i)
        else:
            i += 1

print(len(l))
for i in l:
    print(i, end=' ')
