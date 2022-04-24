# решение задачи отсюда:
# https://stepik.org/lesson/54772/step/7?unit=34222

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
    if l[i] in range(segments[0][0], segments[0][1] + 1):
        l.pop(i)
    else:
        i += 1

print(len(l))
for i in l:
    print(i, end=' ')
