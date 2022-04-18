
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://codeforces.com/problemset/problem/1165/A
n, k = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(n)]
segments_covering_point = [0] * (2 * (10 ** 5) + 1)
positions_to_remove = []
segments_to_remove = []
for i in range(n):
    for j in range(segments[i][0], segments[i][1] + 1):
        segments_covering_point[j] += 1
for i in range(2 * (10 ** 5) + 1):
    if segments_covering_point[i] > k:
        positions_to_remove.append(i)
for position in positions_to_remove:
    for i in range(n):
        if segments[i][0] <= position and position <= segments[i][1]:
            segments_to_remove.append(i + 1)
            break
for segment in segments_to_remove:
    segments.remove(segments[segment - 1])
print(len(segments_to_remove))
for i in range(len(segments_to_remove)):
    print(segments_to_remove[i], end = " ")
