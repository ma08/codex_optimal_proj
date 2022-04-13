
# coding=utf8

def minDist(n, p, distances):
	distances = sorted(distances)
	result = distances[0]
	for i in range(1, n):
		if distances[i] - distances[i-1] > result + p * i:
			result = distances[i] - p * i
	return result

n, p = map(int, raw_input().split())
distances = map(int, raw_input().split())
print minDist(n, p, distances)
