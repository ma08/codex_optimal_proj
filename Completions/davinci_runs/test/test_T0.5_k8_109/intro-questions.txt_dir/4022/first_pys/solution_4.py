

n = int(input())
segments = []

for i in range(n):
    segments.append(list(map(int, input().split())))

segments.sort(key=lambda x: x[0])

lengths = []
for i in range(n):
    if segments[i][0] <= segments[i-1][1]:
        lengths.append(segments[i][1] - segments[i-1][0])
    else:
        lengths.append(segments[i][1] - segments[i][0])

print(max(lengths))