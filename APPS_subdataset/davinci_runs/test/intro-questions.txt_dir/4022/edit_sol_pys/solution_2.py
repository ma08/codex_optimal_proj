
# 
n = int(raw_input())

segments = []
for i in xrange(n):
    segments.append(map(int, raw_input().split()))

segments = sorted(segments, key=lambda x: x[1])

result = float("-inf")

for i in xrange(n):
    left = segments[i][0]
    right = segments[i][1]
    max_right = right
    max_left = left
    for j in xrange(i + 1, n):
        if segments[j][0] <= right:
            max_left = max(max_left, segments[j][0])
        else:
            break
    for j in xrange(i - 1, -1, -1):
        if segments[j][1] >= left:
            max_right = min(max_right, segments[j][1])
        else:
            break
    result = max(max_right - max_left, result)

print result
