
 
n, m = [int(i) for i in input().split()]

segments = []

for i in range(n):
    segments.append([int(i) for i in input().split()])

segments.sort(key=lambda x: x[1])

k = 0

for i in range(m):
    if i+1 not in range(segments[k][0], segments[k][1]+1):
        print(i+1, end=' ')
    elif k+1 < len(segments) and i+1 == segments[k][1]:
        k += 1

print()
