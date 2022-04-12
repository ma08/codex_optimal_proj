import sys

n, p = map(int, sys.stdin.readline().split())
distances = sorted(map(int, sys.stdin.readline().split()))

#print(n, p, distances)

max_distance = max(distances)

min_distance = max_distance

for i in range(len(distances)):
	if distances[i] <= (i+1)*p:
		min_distance = min(min_distance, distances[i])
	else:
		break

print(min_distance)
