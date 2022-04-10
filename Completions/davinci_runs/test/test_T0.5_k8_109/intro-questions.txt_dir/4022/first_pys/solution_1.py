

n = int(input())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))

# sort by left and right
segments = sorted(segments, key=lambda x: x[0])
segments = sorted(segments, key=lambda x: x[1])

# find the maximum length of the intersection of all segments
max_length = segments[0][1] - segments[0][0]
for i in range(1, n):
    if segments[i][0] <= max_length:
        max_length = segments[i][1] - segments[i][0]
    else:
        max_length = segments[i][0] - segments[i - 1][1]

# find the maximum length of the intersection of all segments - 1
max_length_1 = 0
for i in range(n):
    if i == 0:
        length = segments[i + 1][1] - segments[i + 1][0]
    elif i == n - 1:
        length = segments[i - 1][1] - segments[i - 1][0]
    else:
        length = max(segments[i - 1][1] - segments[i - 1][0], segments[i + 1][1] - segments[i + 1][0])
    if length > max_length_1:
        max_length_1 = length

print(max_length_1)