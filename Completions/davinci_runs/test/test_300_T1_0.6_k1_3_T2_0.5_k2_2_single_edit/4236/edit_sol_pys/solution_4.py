


def find_points(segments):
    l = []
    for i in range(len(segments)):
        for j in range(segments[i][0], segments[i][1] + 1):
            l.append(j)
    l = list(set(l))
    l.sort()

    i = 0
    while i < len(l):
        if l[i] in range(segments[i][0], segments[i][1] + 1):
            l.pop(i)
        else:
            i += 1
    return l


n, m = map(int, input().split())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))

l = find_points(segments)

print(len(l))
for i in l:
    print(i, end=' ')
