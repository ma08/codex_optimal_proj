

n = int(input())
segments = []
for i in range(n):
    segments.append([int(x) for x in input().split()])
segments.sort()

#print(segments)

last = segments[0][1]
segments.pop(0)

for segment in segments:
    if segment[0] <= last:
        last = min(segment[1], last)
    else:
        break

print(last)